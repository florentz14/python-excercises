# -------------------------------------------------
# File Name: 23_simplify_path.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Simplify Unix-style file paths using stack.
# -------------------------------------------------

"""
============================================================
  SIMPLIFY PATH - Python 3.14
  Given an absolute Unix-style path, return its canonical form.

  Rules:
    - "." means current directory (ignore).
    - ".." means go to parent directory (pop if possible).
    - Multiple slashes are treated as one slash.

  Example:
    "/a/./b/../../c/" -> "/c"

  Technique:
    - Split by "/"
    - Process parts with a stack
    - Join with single slashes
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def simplify_path(path: str) -> str:
    """Return canonical Unix path."""
    stack: list[str] = []

    for part in path.split("/"):
        if part == "" or part == ".":
            continue
        if part == "..":
            if stack:
                stack.pop()
            continue
        stack.append(part)

    return "/" + "/".join(stack)


def demo() -> None:
    title("SIMPLIFY PATH - Stack-based normalization")

    tests = [
        ("/home/", "/home"),
        ("/../", "/"),
        ("/home//foo/", "/home/foo"),
        ("/a/./b/../../c/", "/c"),
        ("/a/../../b/../c//.//", "/c"),
        ("/a//b////c/d//././/..", "/a/b/c"),
    ]

    for raw, expected in tests:
        result = simplify_path(raw)
        print(f"\n  Input   : {raw}")
        print(f"  Result  : {result}")
        print(f"  Expected: {expected}")
        print(f"  Match   : {result == expected}")


if __name__ == "__main__":
    demo()
