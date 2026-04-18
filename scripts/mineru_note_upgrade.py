#!/usr/bin/env python3

from __future__ import annotations

import ast
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from pypdf import PdfReader


ROOT = Path("/Users/elgask0/REPOS/thesis")
LIT_DIR = ROOT / "02_literature"
PDF_DIR = LIT_DIR / "pdf"
NOTES_DIR = LIT_DIR / "summaries"
MASTER_PATH = LIT_DIR / "literature_master.md"
PARSED_DIR = LIT_DIR / "parsed"
REPORT_PATH = LIT_DIR / "mineru_note_upgrade_report.md"
MINERU_BIN = ROOT / ".venv-mineru" / "bin" / "mineru"

STUB_MARKERS = (
    "_to fill during close read_",
    "_page / quote_",
    "_none noted in master file_",
    "_link sibling notes_",
    "_how this paper supports specific claims / sections_",
)

LANG_OVERRIDES = {
    "caict_2023_computing_power_index": "ch",
    "caict_2024_green_computing_report": "ch",
    "ndrc_2023_edwc_integrated_computing_network": "ch",
    "ndrc_miit_nea_nda_2024_green_datacenter_action_plan": "ch",
}

# Large reports and long appendices get a bounded parse window. The workflow
# records these as partial parses and falls back to direct PDF text when needed.
PAGE_CAPS = {
    "iea_2025_energy_and_ai": 60,
    "shehabi_2024_us_dc_energy_report": 50,
    "green_grid_2012_pue_wp49": 40,
    "caict_2023_computing_power_index": 40,
    "caict_2024_green_computing_report": 50,
    "kline_moretti_2014_tva_big_push": 40,
    "greenstone_2010_plant_openings_spillovers": 40,
    "busso_2013_place_based_policy": 40,
}

NOISE_MARKERS = [
    "Contents lists available",
    "Keywords:",
    "a r t i c l e i n f o",
    "图 目 录",
    "图 11",
    "Implementation Opinions on Deepening",
]


@dataclass
class Paper:
    stem: str
    note_path: Path
    pdf_path: Path
    parsed_md_path: Path
    parsed_content_path: Path
    page_count: int
    parse_page_cap: int | None
    parse_kind: str
    lang: str
    frontmatter: dict
    title: str
    role_in_proposal: str
    use_in_proposal: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def parse_master_stems(master_text: str) -> list[str]:
    return re.findall(r"\*\*Filename:\*\* `([^`]+)`", master_text)


def parse_frontmatter(note_text: str) -> tuple[dict, str]:
    parts = note_text.split("---", 2)
    if len(parts) < 3:
        return {}, note_text
    fm_text = parts[1]
    body = parts[2].lstrip("\n")
    frontmatter: dict[str, object] = {}
    for raw_line in fm_text.splitlines():
        line = raw_line.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            frontmatter[key] = value[1:-1]
        elif value.startswith("[") and value.endswith("]"):
            try:
                frontmatter[key] = ast.literal_eval(value)
            except Exception:
                frontmatter[key] = value
        else:
            frontmatter[key] = value
    return frontmatter, body


def dump_frontmatter(frontmatter: dict) -> str:
    lines = ["---"]
    preferred_order = [
        "filename_stem",
        "citation",
        "first_author",
        "year",
        "title",
        "venue",
        "doi",
        "url",
        "stream",
        "subsection",
        "tags",
        "proposal_sections",
        "cpc_component",
        "priority",
        "caveat",
        "zotero_key",
        "pdf_local",
        "note_status",
    ]
    emitted = set()
    for key in preferred_order:
        if key in frontmatter:
            lines.append(format_frontmatter_line(key, frontmatter[key]))
            emitted.add(key)
    for key in sorted(k for k in frontmatter if k not in emitted):
        lines.append(format_frontmatter_line(key, frontmatter[key]))
    lines.append("---")
    return "\n".join(lines)


def format_frontmatter_line(key: str, value: object) -> str:
    if isinstance(value, list):
        return f'{key}: {json.dumps(value, ensure_ascii=False)}'
    if isinstance(value, int):
        return f"{key}: {value}"
    return f'{key}: "{str(value).replace(chr(34), r"\"")}"'


def parse_note_sections(body: str) -> dict[str, str]:
    headings = re.findall(r"^## .+$", body, flags=re.M)
    sections: dict[str, str] = {}
    for idx, heading in enumerate(headings):
        start = body.index(heading)
        end = body.index(headings[idx + 1], start) if idx + 1 < len(headings) else len(body)
        sections[heading] = body[start:end].rstrip()
    return sections


def section_content(body: str, heading: str) -> str:
    pattern = rf"(^## {re.escape(heading)}\n)(.*?)(?=^## |\Z)"
    match = re.search(pattern, body, flags=re.S | re.M)
    return match.group(2).strip() if match else ""


def replace_section(body: str, heading: str, new_content: str) -> str:
    pattern = rf"(^## {re.escape(heading)}\n)(.*?)(?=^## |\Z)"
    replacement = rf"\1{new_content.strip()}\n\n"
    if re.search(pattern, body, flags=re.S | re.M):
        return re.sub(pattern, replacement, body, count=1, flags=re.S | re.M)
    return body.rstrip() + f"\n\n## {heading}\n{new_content.strip()}\n"


def infer_parse_cap(stem: str, page_count: int) -> tuple[int | None, str]:
    if stem in PAGE_CAPS:
        cap = min(page_count, PAGE_CAPS[stem])
        return cap, "partial" if cap < page_count else "full"
    if page_count > 80:
        return 40, "partial"
    return None, "full"


def parse_papers() -> list[Paper]:
    master_text = read_text(MASTER_PATH)
    stems = [Path(name).stem for name in parse_master_stems(master_text)]
    papers: list[Paper] = []
    for stem in stems:
        note_path = NOTES_DIR / f"{stem}.md"
        pdf_path = PDF_DIR / f"{stem}.pdf"
        note_text = read_text(note_path)
        frontmatter, body = parse_frontmatter(note_text)
        page_count = len(PdfReader(str(pdf_path)).pages)
        cap, parse_kind = infer_parse_cap(stem, page_count)
        parsed_md_path = PARSED_DIR / stem / "txt" / f"{stem}.md"
        parsed_content_path = PARSED_DIR / stem / "txt" / f"{stem}_content_list.json"
        papers.append(
            Paper(
                stem=stem,
                note_path=note_path,
                pdf_path=pdf_path,
                parsed_md_path=parsed_md_path,
                parsed_content_path=parsed_content_path,
                page_count=page_count,
                parse_page_cap=cap,
                parse_kind=parse_kind,
                lang=LANG_OVERRIDES.get(stem, "en"),
                frontmatter=frontmatter,
                title=str(frontmatter.get("title", stem)),
                role_in_proposal=section_content(body, "Role in proposal"),
                use_in_proposal=section_content(body, "Use in proposal"),
            )
        )
    return papers


def ensure_mineru_available() -> None:
    if not MINERU_BIN.exists():
        raise FileNotFoundError(f"MinerU binary not found at {MINERU_BIN}")


def should_run_parse(paper: Paper) -> bool:
    if not paper.parsed_md_path.exists():
        return True
    md = read_text(paper.parsed_md_path)
    return len(md.strip()) < 1000


def run_mineru_parse(paper: Paper) -> tuple[str, bool, str]:
    if not paper.pdf_path.exists():
        return "missing_pdf", False, "PDF missing from corpus directory."
    if not should_run_parse(paper):
        return paper.parse_kind, False, "Existing parsed Markdown reused."

    cmd = [
        str(MINERU_BIN),
        "-p",
        str(paper.pdf_path),
        "-o",
        str(PARSED_DIR),
        "-b",
        "pipeline",
        "-m",
        "txt",
        "-l",
        paper.lang,
        "-f",
        "False",
        "-t",
        "False",
    ]
    if paper.parse_page_cap is not None and paper.parse_page_cap < paper.page_count:
        cmd.extend(["-e", str(paper.parse_page_cap - 1)])

    env = os.environ.copy()
    env.update(
        {
            "HF_HUB_DISABLE_XET": "1",
            "HF_HUB_ENABLE_HF_TRANSFER": "0",
            "MINERU_VIRTUAL_VRAM_SIZE": "16",
            "MINERU_PDF_RENDER_THREADS": "8",
        }
    )
    proc = subprocess.run(
        cmd,
        cwd=str(ROOT),
        env=env,
        capture_output=True,
        text=True,
        timeout=3600,
    )
    if proc.returncode != 0:
        tail = "\n".join((proc.stderr or proc.stdout).splitlines()[-8:])
        return "parse_fail", False, tail or "MinerU exited with a non-zero status."
    if not paper.parsed_md_path.exists():
        return "parse_fail", False, "MinerU exited cleanly but no Markdown file was produced."
    return paper.parse_kind, False, "MinerU parse completed."


def clean_markdown_text(md_text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", md_text)
    text = re.sub(r"^#+\s+", "", text, flags=re.M)
    cut_markers = [
        r"\n## REFERENCES\b",
        r"\n## ACKNOWLEDGMENTS\b",
        r"\nREFERENCES\b",
        r"\nACKNOWLEDGMENTS\b",
        r"\nARTICLE TOOLS\b",
        r"\nPERMISSIONS\b",
    ]
    for marker in cut_markers:
        match = re.search(marker, text, flags=re.I)
        if match:
            text = text[: match.start()]
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\b([A-Za-z])-\s+([A-Za-z])", r"\1\2", text)
    return text.strip()


def extract_pdf_text(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    chunks = []
    for page in reader.pages[: min(len(reader.pages), 80)]:
        try:
            chunks.append(page.extract_text() or "")
        except Exception:
            continue
    text = "\n".join(chunks)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_sentences(text: str) -> list[str]:
    text = text.replace(" e.g. ", " eg ")
    raw = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text)
    cleaned = []
    for sentence in raw:
        sentence = sentence.strip(" -\n\t")
        sentence = re.sub(r"\s+", " ", sentence)
        if len(sentence) >= 40:
            cleaned.append(sentence)
    return cleaned


def is_usable_sentence(sentence: str) -> bool:
    stripped = sentence.strip()
    if len(stripped) < 50:
        return False
    if stripped[0].islower():
        return False
    if any(
        bad in stripped
        for bad in [
            "Keywords:",
            "journal homepage",
            "Received ",
            "Available online",
            "United States of America",
            "Contents lists available",
            "Article history:",
        ]
    ):
        return False
    if re.search(r"^(Step|Section|Fig\.|Figure|Table)\b", stripped):
        return False
    if re.search(r"[=∑δβ_]{2,}", stripped):
        return False
    if stripped.count("(") > 3 and stripped.count(")") > 3:
        return False
    if stripped.endswith(":"):
        return False
    return True


def clean_sentence_list(sentences: Iterable[str]) -> list[str]:
    return [sentence for sentence in sentences if is_usable_sentence(sentence)]


def make_indexed_items(sentences: list[str]) -> list[dict]:
    return [{"text": sentence, "page": None, "rank": idx} for idx, sentence in enumerate(sentences)]


def load_content_items(content_path: Path) -> list[dict]:
    if not content_path.exists():
        return []
    try:
        return json.loads(read_text(content_path))
    except Exception:
        return []


def sentence_items_from_content(content_items: Iterable[dict]) -> list[dict]:
    items = []
    for block in content_items:
        if block.get("type") != "text":
            continue
        text = re.sub(r"\s+", " ", str(block.get("text", "")).strip())
        if not text:
            continue
        for sentence in split_sentences(text):
            if not is_usable_sentence(sentence):
                continue
            items.append(
                {
                    "text": sentence,
                    "page": int(block.get("page_idx", -1)) + 1 if block.get("page_idx") is not None else None,
                }
            )
    return items


def extract_summary_region(text: str) -> str:
    region = text
    markers = [r"\ba b s t r a c t\b", r"\babstract\b"]
    for marker in markers:
        match = re.search(marker, region, flags=re.I)
        if match:
            region = region[match.end():]
            break
    end_markers = [r"\b1\.\s*Introduction\b", r"\bIntroduction\b", r"\bREFERENCES\b"]
    for marker in end_markers:
        match = re.search(marker, region, flags=re.I)
        if match and match.start() > 300:
            region = region[: match.start()]
            break
    return region[:5000]


def select_sentences(items: list[dict], keywords: Iterable[str], limit: int = 4, max_words: int | None = None) -> list[dict]:
    keywords = [k.lower() for k in keywords]
    scored = []
    seen = set()
    for item in items:
        sentence = item["text"].strip()
        norm = sentence.lower()
        if norm in seen:
            continue
        if max_words is not None and len(sentence.split()) > max_words:
            continue
        score = 0
        if any(k in norm for k in keywords):
            score += 3
        if re.search(r"\d", sentence):
            score += 1
        if 60 <= len(sentence) <= 260:
            score += 1
        rank = item.get("rank")
        if isinstance(rank, int):
            score += max(0, 4 - (rank // 3))
        if score > 0:
            scored.append((score, item))
            seen.add(norm)
    scored.sort(key=lambda tup: (-tup[0], len(tup[1]["text"])))
    return [item for _, item in scored[:limit]]


def determine_paper_type(paper: Paper) -> str:
    title = paper.title.lower()
    stem = paper.stem
    stream = str(paper.frontmatter.get("stream", "")).lower()
    if any(word in title for word in ["difference-in-differences", "event-study", "event studies", "synthetic control", "two-way fixed effects"]):
        return "methods paper"
    if stem.startswith(("ndrc_", "caict_", "iea_", "rmi_", "greenpeace_", "shehabi_")):
        return "policy or technical report"
    if any(word in title for word in ["specification", "methodology", "benchmark", "white paper", "standard"]):
        return "standard or benchmark methodology"
    if "scenario" in title or "simulation" in title:
        return "simulation or scenario paper"
    if stream == "design":
        return "empirical or methods paper"
    if stream == "measurement":
        return "measurement or accounting paper"
    if stream == "china context":
        return "context or institutional paper"
    return "empirical paper"


def summarize_core(paper: Paper, parsed_text: str, sentence_items: list[dict]) -> str:
    primary_sentences = clean_sentence_list(split_sentences(extract_summary_region(parsed_text)))
    paper_type = determine_paper_type(paper)
    if paper_type == "methods paper":
        core_keywords = [
            "show",
            "propose",
            "contaminated",
            "heterogeneous treatment",
            "pretrends",
            "weights",
            "alternative estimator",
        ]
    elif paper_type in {"policy or technical report", "standard or benchmark methodology"}:
        core_keywords = [
            "report",
            "estimate",
            "documents",
            "find",
            "projection",
            "benchmark",
            "standard",
            "specification",
        ]
    else:
        core_keywords = [
            "find",
            "show",
            "estimate",
            "argue",
            "suggest",
            "conclude",
            "demonstrate",
            "plateau",
            "reduction",
            "increase",
            "policy",
            "carbon",
            "electricity",
            "bottom-up",
        ]
    core_candidates = select_sentences(
        make_indexed_items(primary_sentences),
        keywords=core_keywords,
        limit=4,
    )
    bullets = []
    title = paper.title
    role = paper.role_in_proposal.strip()
    if role:
        bullets.append(role)
    if core_candidates:
        bullets.extend(unique_texts([item["text"] for item in core_candidates], max_items=3))
    else:
        first_sentence = clean_sentence_list(split_sentences(parsed_text[:1800]))
        if first_sentence:
            bullets.append(first_sentence[0])
        else:
            bullets.append(f"The paper develops the argument signaled by its title, {title}.")
    return "\n".join(f"- {trim_bullet_text(bullet)}" for bullet in bullets[:4])


def summarize_method(paper: Paper, parsed_text: str, sentence_items: list[dict]) -> str:
    primary_sentences = clean_sentence_list(split_sentences(extract_summary_region(parsed_text)))
    paper_type = determine_paper_type(paper)
    if paper_type == "methods paper":
        method_keywords = [
            "difference-in-differences",
            "two-way fixed effects",
            "event study",
            "estimator",
            "weights",
            "application",
            "consider a setting",
            "define",
        ]
    elif paper_type == "policy or technical report":
        method_keywords = [
            "report",
            "survey",
            "projection",
            "inventory",
            "compiles",
            "documents",
            "benchmark",
            "scenario",
        ]
    elif paper_type == "standard or benchmark methodology":
        method_keywords = [
            "benchmark",
            "methodology",
            "measurement",
            "specification",
            "standard",
            "power",
            "reporting",
        ]
    else:
        method_keywords = [
            "bottom-up",
            "data",
            "sample",
            "using",
            "we use",
            "combine",
            "combines",
            "we estimate",
            "simulation",
            "benchmark",
            "inventory",
            "scenario",
            "panel",
            "lmdi",
            "survey",
            "Cisco",
            "Lawrence Berkeley",
            "PUE",
            "hyperscale",
        ]
    method_candidates = select_sentences(
        make_indexed_items(primary_sentences),
        keywords=method_keywords,
        limit=4,
    )
    bullets = [f"Paper type: {paper_type}."]
    if paper.page_count:
        if paper.parse_page_cap and paper.parse_page_cap < paper.page_count:
            bullets.append(
                f"Parsed coverage used here: pages 1-{paper.parse_page_cap} of {paper.page_count} total pages."
            )
        else:
            bullets.append(f"Parsed coverage used here: full document ({paper.page_count} pages).")
    role_lower = paper.role_in_proposal.lower()
    if "bottom-up" in role_lower:
        bullets.append("The paper uses a bottom-up accounting approach rather than a reduced-form causal design.")
    if paper_type == "methods paper":
        bullets.append("The contribution is formal identification and estimation logic rather than a new sector-specific dataset.")
    if paper_type == "policy or technical report":
        bullets.append("The source compiles institutional, technical, or projection material rather than estimating a causal treatment effect.")
    if method_candidates:
        bullets.extend(unique_texts([item["text"] for item in method_candidates], max_items=3))
    elif paper.use_in_proposal.strip():
        bullets.append(paper.use_in_proposal.strip())
    return "\n".join(f"- {trim_bullet_text(bullet)}" for bullet in bullets[:5])


def build_quotes(paper: Paper, sentence_items: list[dict]) -> tuple[str, bool]:
    quote_candidates = select_sentences(
        sentence_items,
        keywords=[
            "data center",
            "electricity",
            "carbon",
            "compute",
            "energy",
            "event study",
            "difference-in-differences",
            "synthetic control",
            "PUE",
            "benchmark",
            "China",
            "provincial",
        ],
        limit=5,
        max_words=25,
    )
    lines = []
    for item in quote_candidates[:3]:
        page = item.get("page")
        prefix = f"- p. {page}: " if page and page > 0 else "- "
        lines.append(f'{prefix}"{item["text"]}"')
    if not lines:
        return "- No short quote with a stable page anchor was recovered from the MinerU content list; use the PDF directly if exact wording is needed.", True
    return "\n".join(lines), False


def build_relevance(paper: Paper) -> str:
    proposal_sections = str(paper.frontmatter.get("proposal_sections", "")).strip()
    stream = str(paper.frontmatter.get("stream", "")).strip()
    uses = []
    sections_lower = proposal_sections.lower()
    if "§1" in proposal_sections:
        uses.append("background")
    if "§2" in proposal_sections:
        uses.append("literature review")
    if "gap" in (paper.role_in_proposal + " " + paper.use_in_proposal).lower() or "§2.4" in proposal_sections:
        uses.append("research gap")
    if "§3.4" in proposal_sections or stream == "Design":
        uses.append("empirical strategy")
    if "§2.3" in proposal_sections or "§3.2" in proposal_sections or "§3.4.3" in proposal_sections or stream == "Measurement":
        uses.append("CPC / measurement logic")
    if stream == "China context" or "§1.1.3" in proposal_sections or "§1.1.4" in proposal_sections or "§3.5" in proposal_sections:
        uses.append("China contextual interpretation")
    use_list = ", ".join(unique_texts(uses, max_items=6)) if uses else "section use still needs manual assignment"
    bullets = []
    if paper.role_in_proposal.strip():
        bullets.append(paper.role_in_proposal.strip())
    if proposal_sections:
        bullets.append(f"Proposal placement: {proposal_sections}")
    bullets.append(f"Most relevant use within the proposal: {use_list}.")
    return "\n".join(f"- {trim_bullet_text(bullet)}" for bullet in bullets)


def build_caveats(paper: Paper, parse_status: str, fallback_used: bool) -> str:
    caveats = []
    paper_type = determine_paper_type(paper)
    title = paper.title.lower()
    if "scenario" in title or "simulation" in title or paper.stem in {"zhang_duan_2025_edwc_net_zero", "xie_2024_ewcrt_co2_reduction", "zhang_li_wang_2025_edwc_bits_migration"}:
        caveats.append("Use this as simulation or scenario evidence, not as ex post causal evidence on realized EDWC outcomes.")
    if paper_type in {"policy or technical report", "standard or benchmark methodology"}:
        caveats.append("This is an institutional or technical source rather than peer-reviewed causal evidence.")
    if str(paper.frontmatter.get("stream", "")).lower() == "design":
        caveats.append("Use it to justify identification strategy or estimator choice, not as direct evidence on EDWC or China data centers.")
    if str(paper.frontmatter.get("stream", "")).lower() == "china context":
        caveats.append("Use it to discipline interpretation and mechanism discussion rather than to identify EDWC effects directly.")
    if parse_status == "partial" and paper.parse_page_cap is not None:
        caveats.append(
            f"The MinerU parse covers pages 1-{paper.parse_page_cap} only; later appendices or back matter may still require direct PDF follow-up."
        )
    if fallback_used:
        caveats.append("Some note content below uses direct PDF text because the MinerU output was too thin or too noisy for that section.")
    if not caveats and paper.frontmatter.get("caveat"):
        caveats.append(str(paper.frontmatter["caveat"]))
    if not caveats:
        caveats.append("No major citation-use caveat beyond the paper's own scope is obvious from the current parse.")
    return "\n".join(f"- {trim_bullet_text(caveat)}" for caveat in unique_texts(caveats, max_items=4))


def unique_texts(values: Iterable[str], max_items: int) -> list[str]:
    seen = set()
    result = []
    for value in values:
        clean = trim_bullet_text(value)
        if not clean:
            continue
        key = clean.lower()
        if key in seen:
            continue
        seen.add(key)
        result.append(clean)
        if len(result) >= max_items:
            break
    return result


def trim_bullet_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip(" -")
    return text


def build_related_section(paper: Paper, papers: list[Paper]) -> str:
    scores = []
    paper_tags = set(paper.frontmatter.get("tags", []) or [])
    for other in papers:
        if other.stem == paper.stem:
            continue
        score = 0
        reason = []
        if paper.frontmatter.get("subsection") == other.frontmatter.get("subsection"):
            score += 4
            reason.append("same subsection")
        if paper.frontmatter.get("stream") == other.frontmatter.get("stream"):
            score += 2
            reason.append("same stream")
        overlap = sorted(paper_tags & set(other.frontmatter.get("tags", []) or []))
        if overlap:
            score += len(overlap)
            reason.append("shared tags: " + ", ".join(overlap[:3]))
        if score > 0:
            scores.append((score, other, "; ".join(reason)))
    scores.sort(key=lambda tup: (-tup[0], tup[1].stem))
    lines = []
    for _, other, reason in scores[:4]:
        lines.append(f"- [{other.stem}.md]({other.stem}.md): {reason}.")
    if not lines:
        lines.append("- No close sibling note was identified automatically; use the master file to add a tighter comparison if needed.")
    return "\n".join(lines)


def build_note_status(parse_status: str, fallback_used: bool) -> str:
    suffix = "pdf-fallback" if fallback_used else "mineru"
    return f"upgraded-{suffix}-{parse_status}"


def section_has_noise(text: str) -> bool:
    if any(marker in text for marker in NOISE_MARKERS):
        return True
    if len(re.findall(r"\d", text)) > 25 and ("图" in text or "Figure" in text):
        return True
    return False


def upgrade_note(paper: Paper, papers: list[Paper], parse_status: str) -> tuple[list[str], bool, bool, str]:
    original_text = read_text(paper.note_path)
    frontmatter, body = parse_frontmatter(original_text)
    parsed_text = read_text(paper.parsed_md_path) if paper.parsed_md_path.exists() else ""
    content_items = load_content_items(paper.parsed_content_path)
    cleaned_text = clean_markdown_text(parsed_text)
    fallback_used = False
    if len(cleaned_text) < 1800:
        cleaned_text = extract_pdf_text(paper.pdf_path)
        fallback_used = True
    sentence_items = sentence_items_from_content(content_items)
    if not sentence_items:
        fallback_sentence_items = [{"text": s, "page": None} for s in split_sentences(cleaned_text[:12000])]
        sentence_items = fallback_sentence_items
        fallback_used = True

    sections_upgraded = []
    core = summarize_core(paper, cleaned_text, sentence_items)
    method = summarize_method(paper, cleaned_text, sentence_items)
    quotes, quote_gap = build_quotes(paper, sentence_items)
    relevance = build_relevance(paper)
    caveats = build_caveats(paper, parse_status, fallback_used)
    related = build_related_section(paper, papers)

    replacements = {
        "Core argument / findings": core,
        "Method & data": method,
        "Key quotes": quotes,
        "Relevance to EDWC thesis": relevance,
        "Caveats / limitations": caveats,
        "Related papers in corpus": related,
    }
    for heading, content in replacements.items():
        body = replace_section(body, heading, content)
        sections_upgraded.append(heading)

    frontmatter["note_status"] = build_note_status(parse_status, fallback_used)
    updated_text = dump_frontmatter(frontmatter) + "\n\n" + body.strip() + "\n"
    write_text(paper.note_path, updated_text)

    reason = ""
    needs_review = False
    if parse_status in {"parse_fail", "parse_poor"}:
        needs_review = True
        reason = "MinerU parse failed or stayed too weak; note leans on PDF fallback."
    elif parse_status == "partial":
        needs_review = True
        reason = f"Only pages 1-{paper.parse_page_cap} were parsed by MinerU; later sections may still matter."
    elif quote_gap:
        needs_review = True
        reason = "Quote extraction stayed thin even after the MinerU pass."
    elif section_has_noise(core) or section_has_noise(method) or section_has_noise(quotes):
        needs_review = True
        reason = "MinerU-selected text still contains header, contents-page, or figure-caption noise that needs manual cleanup."

    return sections_upgraded, fallback_used, needs_review, reason


def build_report(
    papers: list[Paper],
    parse_records: list[dict],
    upgrade_records: list[dict],
    manual_review: list[tuple[str, str]],
    stubbed_before: int,
) -> str:
    total = len(papers)
    pdfs_found = sum(1 for paper in papers if paper.pdf_path.exists())
    notes_found = sum(1 for paper in papers if paper.note_path.exists())
    upgraded_count = len(upgrade_records)

    lines = ["# MinerU Note Upgrade Report", ""]
    lines.extend(
        [
            "## 1. Corpus summary",
            f"- Total canonical papers: {total}",
            f"- PDFs found: {pdfs_found}",
            f"- Notes found: {notes_found}",
            f"- Notes with stub sections before upgrade: {stubbed_before}",
            f"- Notes upgraded: {upgraded_count}",
            "",
            "## 2. MinerU setup",
            "- MinerU was not available at the start of the workflow; it was installed into the repo-local `.venv-mineru` environment.",
            "- Environment used: Python 3.12.9 in `/Users/elgask0/REPOS/thesis/.venv-mineru` on macOS Apple Silicon.",
            '- Commands used: `python3 -m venv .venv-mineru`, `.venv-mineru/bin/pip install -U uv`, `.venv-mineru/bin/uv pip install --python .venv-mineru/bin/python -U "mineru[all]"`.',
            f"- Parsed output location: `{PARSED_DIR}`",
            "",
            "## 3. Parse results",
            "",
            "| paper / citation key | PDF found? | parsed successfully? | fallback to direct PDF needed? | notes |",
            "|---|---|---|---|---|",
        ]
    )
    for record in parse_records:
        lines.append(
            f"| `{record['stem']}` | {'yes' if record['pdf_found'] else 'no'} | {record['parse_status']} | {'yes' if record['fallback_used'] else 'no'} | {record['parse_note']} |"
        )

    lines.extend(
        [
            "",
            "## 4. Note upgrades performed",
            "",
            "| citation key | note filename | sections upgraded | whether parsed Markdown was sufficient | whether PDF fallback was used |",
            "|---|---|---|---|---|",
        ]
    )
    for record in upgrade_records:
        sections = ", ".join(record["sections_upgraded"])
        lines.append(
            f"| `{record['stem']}` | `{record['note_filename']}` | {sections} | {'yes' if record['parsed_markdown_sufficient'] else 'no'} | {'yes' if record['pdf_fallback_used'] else 'no'} |"
        )

    lines.extend(["", "## 5. Notes still needing manual review"])
    if manual_review:
        for stem, reason in manual_review:
            lines.append(f"- `{stem}`: {reason}")
    else:
        lines.append("- None.")

    missing_pdfs = [paper.stem for paper in papers if not paper.pdf_path.exists()]
    missing_notes = [paper.stem for paper in papers if not paper.note_path.exists()]
    parse_failures = [record for record in parse_records if record["parse_status"] in {"parse_fail", "parse_poor", "missing_pdf"}]
    lines.extend(["", "## 6. Missing inputs"])
    if missing_pdfs:
        lines.append("- Missing PDFs: " + ", ".join(f"`{stem}`" for stem in missing_pdfs))
    else:
        lines.append("- Missing PDFs: none.")
    if missing_notes:
        lines.append("- Missing notes: " + ", ".join(f"`{stem}`" for stem in missing_notes))
    else:
        lines.append("- Missing notes: none.")
    if parse_failures:
        lines.append("- Parse failures: " + ", ".join(f"`{record['stem']}`" for record in parse_failures))
    else:
        lines.append("- Parse failures: none.")

    manual_stems = {stem for stem, _ in manual_review}
    ready_lit = "yes" if not (manual_stems & {"zhang_li_wang_2025_edwc_bits_migration", "zhang_duan_2025_edwc_net_zero", "masanet_2020_recalibrating_dc_energy"}) else "mostly"
    ready_background = "yes" if "iea_2025_energy_and_ai" not in manual_stems else "mostly"
    ready_empirical = "yes" if not (manual_stems & {"sun_abraham_2021_event_study_het", "goodman_bacon_2021_did_timing", "wang_2023_uhv_emissions_staggered_did"}) else "mostly"
    ready_cpc = "yes" if not (manual_stems & {"gupta_2022_chasing_carbon", "caict_2024_green_computing_report", "green_grid_2012_pue_wp49"}) else "mostly"
    lines.extend(
        [
            "",
            "## 7. Final readiness",
            f"- Literature review drafting: {ready_lit}",
            f"- Background drafting: {ready_background}",
            f"- Empirical strategy drafting: {ready_empirical}",
            f"- CPC / measurement drafting: {ready_cpc}",
            "",
        ]
    )
    return "\n".join(lines)


def count_stubbed_notes(papers: list[Paper]) -> int:
    count = 0
    for paper in papers:
        text = read_text(paper.note_path)
        if any(marker in text for marker in STUB_MARKERS):
            count += 1
    return count


def main() -> int:
    ensure_mineru_available()
    PARSED_DIR.mkdir(parents=True, exist_ok=True)
    papers = parse_papers()
    selected_stems = set(sys.argv[1:])
    if selected_stems:
        papers = [paper for paper in papers if paper.stem in selected_stems]
        if not papers:
            raise SystemExit(f"No canonical papers matched: {', '.join(sorted(selected_stems))}")
    stubbed_before = count_stubbed_notes(papers)

    parse_records: list[dict] = []
    upgrade_records: list[dict] = []
    manual_review: list[tuple[str, str]] = []

    for paper in papers:
        print(f"[parse] {paper.stem}", flush=True)
        parse_status, fallback_used_during_parse, parse_note = run_mineru_parse(paper)
        if parse_status in {"full", "partial"}:
            md_text = read_text(paper.parsed_md_path) if paper.parsed_md_path.exists() else ""
            if len(md_text.strip()) < 1000:
                parse_status = "parse_poor"
                parse_note = "Parsed Markdown exists but stayed too thin for note use."
        sections_upgraded, note_pdf_fallback, needs_review, reason = upgrade_note(paper, papers, parse_status)
        if needs_review:
            manual_review.append((paper.stem, reason))
        parse_records.append(
            {
                "stem": paper.stem,
                "pdf_found": paper.pdf_path.exists(),
                "parse_status": parse_status,
                "fallback_used": fallback_used_during_parse or note_pdf_fallback,
                "parse_note": parse_note,
            }
        )
        upgrade_records.append(
            {
                "stem": paper.stem,
                "note_filename": paper.note_path.name,
                "sections_upgraded": sections_upgraded,
                "parsed_markdown_sufficient": not note_pdf_fallback,
                "pdf_fallback_used": note_pdf_fallback,
            }
        )

    report_text = build_report(
        papers=papers,
        parse_records=parse_records,
        upgrade_records=upgrade_records,
        manual_review=manual_review,
        stubbed_before=stubbed_before,
    )
    write_text(REPORT_PATH, report_text)

    print()
    print(f"Notes upgraded: {len(upgrade_records)}")
    print(f"Notes still needing manual review: {len(manual_review)}")
    ready = "yes" if len(manual_review) <= 8 else "mostly"
    print(f"Corpus ready for downstream writing: {ready}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
