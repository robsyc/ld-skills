"""Sync HTTP fetching with a simple on-disk cache for local iteration."""

import hashlib
import json
from pathlib import Path
from typing import Optional

import httpx

USER_AGENT = "ld-skills/0.1 (+https://github.com/robsyc/ld-skills)"
DEFAULT_CACHE_DIR = Path(".cache")


class FetchResult:
    def __init__(self, url: str, html: str, final_url: str, from_cache: bool):
        self.url = url
        self.html = html
        self.final_url = final_url
        self.from_cache = from_cache


def _cache_paths(cache_dir: Path, url: str) -> tuple[Path, Path]:
    digest = hashlib.sha256(url.encode()).hexdigest()[:20]
    return cache_dir / f"{digest}.html", cache_dir / f"{digest}.meta.json"


def fetch_html(
    url: str,
    cache_dir: Optional[Path] = None,
    refresh: bool = False,
    timeout: float = 60.0,
) -> FetchResult:
    """Fetch HTML for a URL, using the disk cache when available."""
    cache_dir = cache_dir or DEFAULT_CACHE_DIR
    html_path, meta_path = _cache_paths(cache_dir, url)

    if not refresh and html_path.exists() and meta_path.exists():
        meta = json.loads(meta_path.read_text())
        return FetchResult(url, html_path.read_text(), meta.get("final_url", url), True)

    with httpx.Client(
        timeout=timeout,
        follow_redirects=True,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml",
        },
    ) as client:
        response = client.get(url)
        response.raise_for_status()

    cache_dir.mkdir(parents=True, exist_ok=True)
    html_path.write_text(response.text)
    meta_path.write_text(json.dumps({"url": url, "final_url": str(response.url)}))

    return FetchResult(url, response.text, str(response.url), False)
