#!/usr/bin/env python3
"""Browser-engine wrapper for fetching rendered HTML."""

from __future__ import annotations

from typing import Any


def fetch_source(url: str, engine: str = "safari", **kwargs: Any) -> str:
    """Fetch rendered HTML with the requested browser engine."""

    normalized_engine = engine.lower()
    if normalized_engine == "safari":
        from safari_fetch import fetch_source as safari_fetch_source

        return safari_fetch_source(url, **kwargs)

    if normalized_engine == "chrome":
        from chrome_cdp_fetch import fetch_source as chrome_fetch_source

        delay_seconds = int(kwargs.get("delay_seconds", 8))
        kwargs["delay_seconds"] = max(delay_seconds, 15)
        return chrome_fetch_source(url, **kwargs)

    raise ValueError(f"Unsupported browser engine: {engine}")
