#!/usr/bin/env python3
"""
Commits and pushes new/modified files to the main branch.
Called after any script that generates report files.
"""

import subprocess
import sys


def git_push(message: str, files: list[str]) -> bool:
    try:
        subprocess.run(["git", "add"] + files, check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}", file=sys.stderr)
        return False
