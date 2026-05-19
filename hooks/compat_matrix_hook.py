"""MkDocs hook that auto-generates the ESPHome Compatibility Matrix table.

Fetches release data from the Satellite1-ESPHome GitHub repo at build time
and produces Stable / Beta tabbed tables using pymdownx.tabbed syntax.
Results are cached locally to avoid excessive API calls during development.
"""

import json
import logging
import os
import re
import time
from urllib.error import URLError
from urllib.request import Request, urlopen

log = logging.getLogger("mkdocs.hooks.compat_matrix")

REPO = "FutureProofHomes/Satellite1-ESPHome"
RELEASES_URL = f"https://api.github.com/repos/{REPO}/releases?per_page=100"
RAW_URL = f"https://raw.githubusercontent.com/{REPO}"
ESPHOME_RELEASE_URL = "https://github.com/esphome/esphome/releases/tag"
SAT1_RELEASE_URL = f"https://github.com/{REPO}/releases/tag"

CACHE_DIR = os.path.join(os.path.dirname(__file__), os.pardir, ".cache")
CACHE_FILE = os.path.join(CACHE_DIR, "compat_matrix.json")
DEFAULT_TTL = 3600  # 1 hour

PLACEHOLDER = "<!-- ESPHOME_COMPAT_MATRIX -->"
SHIELDS_URL = "https://img.shields.io/badge"

ESPHOME_RE = re.compile(r"^esphome==(.+)$", re.MULTILINE)
SEMVER_RE = re.compile(r"^v\d+\.\d+\.\d+")
BETA_RE = re.compile(r"-beta\.", re.IGNORECASE)
MIN_MINOR = (0, 1, 0)  # Only show releases >= v0.1.0
MINOR_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+)")


# ── Network helpers ──────────────────────────────────────────────────────────


def _github_headers():
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _fetch_json(url):
    req = Request(url, headers=_github_headers())
    with urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())


def _fetch_text(url):
    req = Request(url, headers=_github_headers())
    with urlopen(req, timeout=10) as resp:
        return resp.read().decode()


def _esphome_version_for_tag(tag):
    """Return the pinned ESPHome version from requirements.txt at *tag*."""
    url = f"{RAW_URL}/{tag}/requirements.txt"
    try:
        text = _fetch_text(url)
    except (URLError, OSError):
        return None
    m = ESPHOME_RE.search(text)
    return m.group(1) if m else None


# ── Caching ──────────────────────────────────────────────────────────────────


def _cache_is_fresh():
    ttl = int(os.environ.get("COMPAT_CACHE_TTL", DEFAULT_TTL))
    if ttl == 0:
        return False
    try:
        age = time.time() - os.path.getmtime(CACHE_FILE)
        return age < ttl
    except OSError:
        return False


def _read_cache():
    try:
        with open(CACHE_FILE) as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return None


def _write_cache(data):
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=2)


# ── Data fetching ────────────────────────────────────────────────────────────


def _fetch_matrix():
    """Fetch all releases and resolve ESPHome versions. Returns dict with
    ``stable`` and ``beta`` lists, each entry being
    ``{"tag": ..., "esphome": ..., "url": ...}``."""
    releases = _fetch_json(RELEASES_URL)

    # Handle pagination – collect up to 5 pages
    all_releases = list(releases)
    page = 2
    while len(releases) == 100 and page <= 5:
        url = f"{RELEASES_URL}&page={page}"
        releases = _fetch_json(url)
        all_releases.extend(releases)
        page += 1

    stable, beta = [], []
    for rel in all_releases:
        if rel.get("draft"):
            continue
        tag = rel["tag_name"]
        if not SEMVER_RE.match(tag):
            continue
        m = MINOR_RE.match(tag)
        if m and tuple(int(x) for x in m.groups()) < MIN_MINOR:
            continue
        esphome = _esphome_version_for_tag(tag)
        if not esphome:
            continue
        entry = {
            "tag": tag,
            "esphome": esphome,
            "url": rel["html_url"],
        }
        if BETA_RE.search(tag):
            beta.append(entry)
        else:
            stable.append(entry)

    return {"stable": stable, "beta": beta}


def _load_matrix():
    """Return the matrix dict, using the cache when possible."""
    if _cache_is_fresh():
        cached = _read_cache()
        if cached:
            log.info("Compat matrix loaded from cache")
            return cached

    try:
        data = _fetch_matrix()
        _write_cache(data)
        log.info(
            "Compat matrix fetched from GitHub (%d stable, %d beta)",
            len(data["stable"]),
            len(data["beta"]),
        )
        return data
    except (URLError, OSError, KeyError) as exc:
        log.warning("Failed to fetch compat matrix from GitHub: %s", exc)
        cached = _read_cache()
        if cached:
            log.info("Falling back to stale cache")
            return cached
        return None


# ── Markdown generation ──────────────────────────────────────────────────────


def _shield_escape(text):
    """Escape characters that shields.io treats as separators."""
    return text.replace("-", "--").replace("_", "__")


def _release_badge(tag, is_beta=False):
    color = "orange" if is_beta else "blue"
    escaped = _shield_escape(tag)
    img = f"{SHIELDS_URL}/release-{escaped}-{color}"
    return f"[![release {tag}]({img})]({SAT1_RELEASE_URL}/{tag})"


def _esphome_badge(version):
    escaped = _shield_escape(version)
    img = f"{SHIELDS_URL}/ESPHome-{escaped}-blue"
    return f"[![ESPHome {version}]({img})]({ESPHOME_RELEASE_URL}/{version})"


def _table_rows(entries, is_beta=False, indent=4):
    prefix = " " * indent
    rows = []
    for e in entries:
        rel_badge = _release_badge(e["tag"], is_beta=is_beta)
        esp_badge = _esphome_badge(e["esphome"])
        rows.append(f"{prefix}| {rel_badge} | {esp_badge} |")
    return rows


def _table_header(indent=4):
    prefix = " " * indent
    return [f"{prefix}| Sat1 Release | ESPHome Version |", f"{prefix}| --- | --- |"]


def _latest_per_minor(entries):
    """Return only the newest entry for each minor version (e.g. v0.1.5)."""
    seen = {}
    result = []
    for e in entries:
        m = MINOR_RE.match(e["tag"])
        if not m:
            continue
        minor_key = m.group(0)  # e.g. "v0.1.5"
        if minor_key not in seen:
            seen[minor_key] = True
            result.append(e)
    return result


def _build_markdown(data):
    lines = []

    lines.append('=== "Stable"')
    lines.append("")
    lines.extend(_table_header(4))
    if data["stable"]:
        lines.extend(_table_rows(data["stable"], is_beta=False, indent=4))
    else:
        lines.append("    | *No stable releases found* | |")
    lines.append("")

    lines.append('=== "Beta"')
    lines.append("")
    if data["beta"]:
        latest = _latest_per_minor(data["beta"])
        lines.extend(_table_header(4))
        lines.extend(_table_rows(latest, is_beta=True, indent=4))
        lines.append("")
        if len(data["beta"]) > len(latest):
            lines.append('    <details markdown="1">')
            lines.append("    <summary>Show all beta releases</summary>")
            lines.append("")
            lines.extend(_table_header(4))
            lines.extend(_table_rows(data["beta"], is_beta=True, indent=4))
            lines.append("")
            lines.append("    </details>")
    else:
        lines.extend(_table_header(4))
        lines.append("    | *No beta releases found* | |")
    lines.append("")

    return "\n".join(lines)


# ── MkDocs hook entry points ────────────────────────────────────────────────


_matrix_data = None


def on_config(config):
    global _matrix_data
    _matrix_data = _load_matrix()
    return config


def on_page_markdown(markdown, page, config, files):
    if PLACEHOLDER not in markdown:
        return markdown
    if _matrix_data is None:
        log.warning(
            "Compat matrix data unavailable; leaving placeholder as-is on %s",
            page.file.src_path,
        )
        return markdown
    return markdown.replace(PLACEHOLDER, _build_markdown(_matrix_data))
