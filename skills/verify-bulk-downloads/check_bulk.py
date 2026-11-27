#!/usr/bin/env python3
"""Bulk-download content verifier, written to test the verify_bulk_downloads skill.

Skill rules implemented:
- Verify content, not status: inspect first bytes, reject files starting with
  HTML markup when an image/binary was expected.
- Flag zero-byte files and files far smaller than the per-library median.
- Keep a manifest with local path, size and detected type for every file.
- Report final good/bad counts; done only when bad == 0 or each bad file
  is named with its cause.
"""
import json
import os
import statistics
import sys

MAGIC = [
    (b"\x89PNG\r\n\x1a\n", "png"),
    (b"\xff\xd8\xff", "jpeg"),
    (b"GIF87a", "gif"),
    (b"GIF89a", "gif"),
]


def detect_type(path):
    """Return (detected_type, cause_or_None). detected_type None means bad."""
    try:
        with open(path, "rb") as f:
            head = f.read(16)
    except OSError as e:
        return None, f"unreadable: {e}"
    if len(head) == 0:
        return None, "zero-byte file"
    stripped = head.lstrip(b"\xef\xbb\xbf \t\r\n")
    low = stripped[:15].lower()
    if low.startswith((b"<!doctype", b"<html", b"<head", b"<body")):
        return None, "starts with HTML markup"
    for magic, kind in MAGIC:
        if head.startswith(magic):
            return kind, None
    if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        return "webp", None
    return None, f"unknown magic bytes: {head[:8]!r}"


def check_library(root):
    files = []
    for dirpath, _dirs, names in os.walk(root):
        for name in names:
            files.append(os.path.join(dirpath, name))
    files.sort()
    # Median per subdirectory: a library can mix full-size files and
    # thumbnails (e.g. portrait/img vs portrait/thumbs) whose sizes differ
    # by an order of magnitude. One median for the whole library would flag
    # every legitimate thumbnail. Group by parent dir relative to the root.
    groups = {}
    for p in files:
        groups.setdefault(os.path.dirname(os.path.relpath(p, root)), []).append(p)
    medians = {
        g: (statistics.median([os.path.getsize(p) for p in ps]) if ps else 0)
        for g, ps in groups.items()
    }
    results = []
    bad = []
    for path in files:
        size = os.path.getsize(path)
        kind, cause = detect_type(path)
        ext = os.path.splitext(path)[1].lower().lstrip(".")
        entry = {
            "path": os.path.relpath(path, root),
            "size": size,
            "detected": kind,
            "extension": ext,
        }
        group = os.path.dirname(os.path.relpath(path, root))
        group_median = medians[group]
        small_threshold = group_median * 0.10 if group_median else 0
        if cause is None and size < small_threshold:
            cause = (
                f"far smaller than median ({size} < 10% of "
                f"{group_median:.0f} in {group or '.'})"
            )
        if cause is not None:
            entry["bad"] = cause
            bad.append(entry)
        results.append(entry)
    return {
        "library": os.path.basename(root.rstrip("/")),
        "total": len(files),
        "good": len(files) - len(bad),
        "bad": len(bad),
        "medians": {g: m for g, m in medians.items()},
        "bad_files": bad,
        "entries": results,
    }


def main():
    target = sys.argv[1]
    out_manifest = sys.argv[2] if len(sys.argv) > 2 else None
    if os.path.isdir(target):
        libraries = sorted(
            os.path.join(target, d)
            for d in os.listdir(target)
            if os.path.isdir(os.path.join(target, d))
        )
        if not libraries:
            libraries = [target]
    else:
        libraries = [target]
    report = {"libraries": [], "total": 0, "good": 0, "bad": 0}
    for lib in libraries:
        r = check_library(lib)
        report["libraries"].append(r)
        report["total"] += r["total"]
        report["good"] += r["good"]
        report["bad"] += r["bad"]
    if out_manifest:
        with open(out_manifest, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=1)
    for lib in report["libraries"]:
        med = ", ".join(
            f"{g or '.'}={m:.0f}B" for g, m in sorted(lib["medians"].items())
        )
        print(
            f"{lib['library']}: total={lib['total']} good={lib['good']} "
            f"bad={lib['bad']} medians[{med}]"
        )
        for b in lib["bad_files"][:20]:
            print(f"  BAD {b['path']} ({b['size']}B): {b['bad']}")
    print(f"TOTAL: {report['total']} good={report['good']} bad={report['bad']}")
    return 0 if report["bad"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
