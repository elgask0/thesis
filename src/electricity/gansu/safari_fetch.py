#!/usr/bin/env python3
"""Fetch rendered HTML from Safari via AppleScript."""

from __future__ import annotations

import subprocess
import time


def _apple_quote(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def fetch_source(url: str, delay_seconds: int = 8, retries: int = 2) -> str:
    """Open a URL in Safari and return the page source.

    This is a browser-assisted fallback for sites that block direct HTTP scraping.
    """

    escaped_url = _apple_quote(url)
    script = [
        '-e', 'tell application "Safari" to activate',
        '-e', 'tell application "Safari" to if (count of documents) = 0 then make new document',
        '-e', f'tell application "Safari" to set URL of front document to "{escaped_url}"',
        '-e', f'delay {delay_seconds}',
        '-e', 'tell application "Safari" to get source of document 1',
    ]

    last_error: RuntimeError | None = None
    for attempt in range(retries + 1):
        completed = subprocess.run(
            ["osascript", *script],
            capture_output=True,
            text=True,
        )
        if completed.returncode == 0:
            html = completed.stdout
            if html and "<html" in html.lower():
                return html
            last_error = RuntimeError("Safari returned an empty or invalid HTML document.")
        else:
            last_error = RuntimeError(completed.stderr.strip() or "Safari fetch failed.")
        if attempt < retries:
            time.sleep(2)

    raise last_error or RuntimeError("Safari fetch failed.")
