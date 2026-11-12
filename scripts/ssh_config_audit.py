#!/usr/bin/env python3
"""Read-only, best-effort SSH config review. Does not evaluate Include/Match semantics."""
from pathlib import Path
import argparse

RULES = {
    "passwordauthentication": {"yes": "PasswordAuthentication yes"},
    "permitrootlogin": {"yes": "PermitRootLogin yes", "without-password": "PermitRootLogin prohibit-password is preferred spelling for compatible versions"},
    "permitemptypasswords": {"yes": "PermitEmptyPasswords yes"},
}


def audit_config(contents: str) -> list[tuple[int, str]]:
    """Return line numbers and insecure directive messages from a plaintext file."""
    findings: list[tuple[int, str]] = []
    for line_no, line in enumerate(contents.splitlines(), start=1):
        stripped = line.split("#", 1)[0].strip()
        if not stripped:
            continue
        parts = stripped.split()
        if len(parts) < 2:
            continue
        key, value = parts[0].lower(), parts[1].lower()
        message = RULES.get(key, {}).get(value)
        if message:
            findings.append((line_no, message))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="Path to an sshd_config file for offline review")
    args = parser.parse_args()
    try:
        contents = args.file.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        parser.error(str(exc))
    print(f"SSH configuration review: {args.file}")
    findings = audit_config(contents)
    if findings:
        for line_no, issue in findings:
            print(f"[WARN] {issue} (line {line_no})")
    else:
        print("[OK] No targeted insecure directives found in this file.")
    print("[INFO] Static file check only; Match/Include contexts not fully evaluated.")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
