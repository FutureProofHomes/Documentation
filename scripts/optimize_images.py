#!/usr/bin/env python3
"""
Optimize images under a directory: losslessly optimize PNGs and compress
JPG/JPEG (re-save at configurable quality). Originals are kept in a backup
directory. No format conversion (JPG stays JPG; PNG stays PNG).

Re-running is safe: files that are already optimized are not replaced (only
smaller outputs are written). You can run this script anytime to optimize
new or changed images.

Usage:
  python3 scripts/optimize_images.py
  python3 scripts/optimize_images.py --dir docs/assets --backup-dir docs/assets/.originals
  python3 scripts/optimize_images.py --jpeg-quality 80

From repo root. Defaults: --dir docs/assets, --backup-dir docs/assets/.originals,
--jpeg-quality 85.

Requires: Pillow (pip install Pillow).
Optional: OptiPNG (e.g. brew install optipng) for better lossless PNG compression;
the script falls back to Pillow-only if OptiPNG is not installed.
"""

import argparse
import logging
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# Formats we process: PNG (optimize), JPG/JPEG (compress at quality)
PNG_EXTENSIONS = {".png"}
JPEG_EXTENSIONS = {".jpg", ".jpeg"}
RASTER_EXTENSIONS = PNG_EXTENSIONS | JPEG_EXTENSIONS | {".gif", ".bmp", ".webp", ".tiff", ".tif"}
SKIP_EXTENSIONS = {".svg"}

try:
    from PIL import Image
except ImportError:
    Image = None


def setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        format="%(message)s",
        level=level,
    )
    # Reduce Pillow's internal logging (e.g. STREAM/tag debug output)
    logging.getLogger("PIL").setLevel(logging.WARNING)


def find_image_files(root: Path, exclude_dir: Path | None) -> list[Path]:
    """Return image paths in deterministic order: PNGs first, then others by path."""
    root = root.resolve()
    if exclude_dir is not None:
        exclude_dir = exclude_dir.resolve()
    pngs = []
    others = []
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in sorted(filenames):
            path = Path(dirpath) / name
            try:
                rel = path.relative_to(root)
            except ValueError:
                continue
            if exclude_dir is not None:
                try:
                    path.relative_to(exclude_dir)
                    continue  # path is under exclude_dir (e.g. backup)
                except ValueError:
                    pass
            ext = path.suffix.lower()
            if ext in SKIP_EXTENSIONS:
                continue
            if ext in RASTER_EXTENSIONS:
                if ext in PNG_EXTENSIONS:
                    pngs.append(path)
                elif ext in JPEG_EXTENSIONS:
                    others.append(path)
                # other raster (gif, bmp, webp, tiff) skipped for now
    return sorted(pngs) + sorted(others)


def backup_path(asset_root: Path, backup_root: Path, file_path: Path) -> Path:
    """Path in backup dir mirroring relative path under asset root."""
    rel = file_path.relative_to(asset_root)
    return backup_root / rel


def ensure_backup(original_path: Path, backup_path: Path) -> None:
    """Copy original_path to backup_path if backup_path does not exist."""
    if backup_path.exists():
        return
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(original_path, backup_path)
    logging.info("  Backup: %s", backup_path)


def optimize_jpeg(path: Path, out_path: Path, quality: int = 85) -> bool:
    """Re-save JPEG at given quality to out_path. Returns True on success."""
    if Image is None:
        return False
    try:
        with Image.open(path) as im:
            if im.mode in ("RGBA", "P"):
                im = im.convert("RGB")
            im.save(out_path, "JPEG", quality=quality, optimize=True)
        return True
    except Exception as e:
        logging.debug("  JPEG optimize failed: %s", e)
        return False


def optimize_png_with_pillow(path: Path, out_path: Path) -> bool:
    """Optimize PNG using Pillow; write to out_path. Returns True on success."""
    if Image is None:
        return False
    try:
        with Image.open(path) as im:
            im.save(out_path, "PNG", optimize=True)
        return True
    except Exception as e:
        logging.debug("  Pillow optimize failed: %s", e)
        return False


def optimize_png_with_optipng(path: Path, out_path: Path) -> bool:
    """Optimize PNG using OptiPNG CLI if available. Writes to out_path."""
    try:
        # OptiPNG -o2 is a good balance of speed vs compression
        result = subprocess.run(
            ["optipng", "-o2", "-out", str(out_path), str(path)],
            capture_output=True,
            timeout=120,
        )
        return result.returncode == 0 and out_path.exists()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def optimize_png(path: Path, temp_dir: Path) -> Path | None:
    """
    Produce an optimized version of the PNG at path. Writes to a temp file.
    Returns path to the optimized file, or None on failure.
    """
    out = temp_dir / ("opt_" + path.name)
    if optimize_png_with_optipng(path, out):
        return out
    if optimize_png_with_pillow(path, out):
        return out
    return None


def process_file(
    file_path: Path,
    asset_root: Path,
    backup_root: Path,
    temp_dir: Path,
    jpeg_quality: int,
    optimized: list[tuple[Path, int, int]],
    skipped: list[Path],
    errors: list[str],
) -> None:
    """Process one image: optimize PNG or compress JPEG (no format conversion)."""
    ext = file_path.suffix.lower()
    orig_size = file_path.stat().st_size

    if ext in PNG_EXTENSIONS:
        opt_path = optimize_png(file_path, temp_dir)
    elif ext in JPEG_EXTENSIONS:
        out = temp_dir / ("opt_" + file_path.name)
        if not optimize_jpeg(file_path, out, quality=jpeg_quality):
            errors.append(str(file_path))
            return
        opt_path = out
    else:
        return

    if opt_path is None:
        errors.append(str(file_path))
        return
    opt_size = opt_path.stat().st_size

    if opt_size >= orig_size:
        skipped.append(file_path)
        logging.debug("  Skip (already optimized): %s", file_path)
        return

    back_path = backup_path(asset_root, backup_root, file_path)
    ensure_backup(file_path, back_path)
    try:
        shutil.copy2(opt_path, file_path)
        optimized.append((file_path, orig_size, opt_size))
        logging.info("  Optimized: %s (%s -> %s bytes)", file_path, orig_size, opt_size)
    except Exception as e:
        logging.error("  Replace failed for %s: %s", file_path, e)
        errors.append(str(file_path))


def _fmt_bytes(n: int) -> str:
    """Format byte count as human-readable (e.g. 1.2 MB)."""
    if n < 1024:
        return f"{n} B"
    if n < 1024 * 1024:
        return f"{n / 1024:.1f} KB"
    return f"{n / (1024 * 1024):.1f} MB"


def _rel(path: Path, root: Path) -> str:
    """Path relative to root for display."""
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def print_report(
    asset_root: Path,
    backup_root: Path,
    jpeg_quality: int,
    images: list[Path],
    optimized: list[tuple[Path, int, int]],
    skipped: list[Path],
    errors: list[str],
) -> None:
    """Print a detailed report of the run and its results."""
    png_count = sum(1 for p in images if p.suffix.lower() in PNG_EXTENSIONS)
    jpeg_count = sum(1 for p in images if p.suffix.lower() in JPEG_EXTENSIONS)

    total_saved = sum(orig - new for _, orig, new in optimized)
    total_orig_optimized = sum(orig for _, orig, _ in optimized)
    total_new_optimized = sum(new for _, orig, new in optimized)

    sep = "=" * 60
    logging.info("")
    logging.info(sep)
    logging.info("IMAGE OPTIMIZATION REPORT")
    logging.info(sep)
    logging.info("")
    logging.info("Run settings")
    logging.info("  Asset directory:  %s", asset_root)
    logging.info("  Backup directory: %s", backup_root)
    logging.info("  JPEG quality:     %d", jpeg_quality)
    logging.info("")
    logging.info("Input")
    logging.info("  Total images:     %d", len(images))
    logging.info("  PNG:              %d", png_count)
    logging.info("  JPEG/JPG:         %d", jpeg_count)
    logging.info("")
    logging.info("Results")
    logging.info("  Optimized:        %d", len(optimized))
    logging.info("  Skipped:          %d (already optimized)", len(skipped))
    logging.info("  Errors:           %d", len(errors))
    logging.info("")
    if optimized:
        logging.info("Total size change (optimized files only)")
        logging.info("  Before:           %s", _fmt_bytes(total_orig_optimized))
        logging.info("  After:            %s", _fmt_bytes(total_new_optimized))
        logging.info("  Saved:            %s (%.1f%%)", _fmt_bytes(total_saved), (100 * total_saved / total_orig_optimized) if total_orig_optimized else 0)
        logging.info("")
        logging.info("Optimized files (path, before -> after, saved)")
        for path, orig, new in sorted(optimized, key=lambda x: (-(x[1] - x[2]), str(x[0]))):
            saved = orig - new
            pct = (100 * saved / orig) if orig else 0
            rel = _rel(path, asset_root)
            logging.info("  %s", rel)
            logging.info("    %s -> %s  (saved %s, %.0f%%)", _fmt_bytes(orig), _fmt_bytes(new), _fmt_bytes(saved), pct)
        logging.info("")
    if skipped and len(skipped) <= 50:
        logging.info("Skipped (already optimized)")
        for path in sorted(skipped):
            logging.info("  %s", _rel(path, asset_root))
        logging.info("")
    elif skipped:
        logging.info("Skipped (already optimized): %d files (use -v to see per-file skip messages)", len(skipped))
        logging.info("")
    if errors:
        logging.info("Errors")
        for e in errors:
            logging.info("  %s", e)
        logging.info("")
    logging.info(sep)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Optimize PNGs (lossless) and compress JPG/JPEG. Keeps originals in backup dir."
    )
    parser.add_argument(
        "--dir",
        default="docs/assets",
        metavar="PATH",
        help="Directory to scan for images (default: docs/assets)",
    )
    parser.add_argument(
        "--backup-dir",
        default="docs/assets/.originals",
        metavar="PATH",
        help="Directory for original files (default: docs/assets/.originals)",
    )
    parser.add_argument(
        "--jpeg-quality",
        type=int,
        default=85,
        metavar="N",
        help="JPEG quality 1-100 for re-compression (default: 85)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose (debug) logging",
    )
    args = parser.parse_args()

    setup_logging(args.verbose)

    if Image is None:
        logging.error("Pillow is required. Install with: pip install Pillow")
        return 1

    asset_root = Path(args.dir).resolve()
    backup_root = Path(args.backup_dir).resolve()

    if not asset_root.is_dir():
        logging.error("Not a directory: %s", asset_root)
        return 1

    if backup_root == asset_root:
        logging.error("Backup dir must not be the same as the asset dir.")
        return 1

    try:
        backup_root.resolve().relative_to(asset_root)
        exclude = backup_root
    except ValueError:
        exclude = None
    images = find_image_files(asset_root, exclude)
    if not images:
        logging.info("No image files found under %s", asset_root)
        return 0

    if not (1 <= args.jpeg_quality <= 100):
        logging.error("--jpeg-quality must be between 1 and 100")
        return 1

    logging.info("Found %d image(s) under %s", len(images), asset_root)
    optimized: list[tuple[Path, int, int]] = []
    skipped: list[Path] = []
    errors: list[str] = []

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        for path in images:
            process_file(
                path,
                asset_root,
                backup_root,
                temp_path,
                args.jpeg_quality,
                optimized,
                skipped,
                errors,
            )

    print_report(
        asset_root,
        backup_root,
        args.jpeg_quality,
        images,
        optimized,
        skipped,
        errors,
    )

    if errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
