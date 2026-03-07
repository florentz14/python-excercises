# ------------------------------------------------------------
# File: 07_context_manager_exceptions.py
# Chapter: Exceptions - Context Managers (with statement)
#
# Purpose:
#   Handle exceptions when using context managers (with statement).
#   Files, locks, and resources can raise during open/close.
#
# Topics:
#   1. File operations - FileNotFoundError, PermissionError
#   2. Nested context managers
#   3. Suppressing exceptions with contextlib.suppress
#
# Author: Florentino Baez (adapted)
# ------------------------------------------------------------

import os
import tempfile
from contextlib import suppress

# -----------------------------------------------------------------------------
# 1. File operations - Safe read with exception handling
# -----------------------------------------------------------------------------


def read_file_safe(filepath: str) -> str | None:
    """
    Read file contents. Returns content or None on error.
    Handles FileNotFoundError, PermissionError, IOError.
    """
    try:
        with open(filepath, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        return None
    except PermissionError:
        print(f"Error: No permission to read: {filepath}")
        return None
    except OSError as e:
        print(f"Error reading file: {e}")
        return None


def write_file_safe(filepath: str, content: str) -> bool:
    """
    Write content to file. Returns True on success, False on error.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except PermissionError:
        print(f"Error: No permission to write: {filepath}")
        return False
    except OSError as e:
        print(f"Error writing file: {e}")
        return False


# -----------------------------------------------------------------------------
# 2. Nested context managers - Exception in inner block
# -----------------------------------------------------------------------------


def demo_nested_context() -> None:
    """
    Create temp file, write, read. Shows how exceptions propagate
    and that 'with' ensures cleanup even on error.
    """
    try:
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as tmp:
            tmp.write("Hello from temp file\n")
            tmp_path = tmp.name

        content = read_file_safe(tmp_path)
        if content:
            print(f"Read from temp: {content.strip()}")

        # Clean up
        os.unlink(tmp_path)
    except OSError as e:
        print(f"Temp file error: {e}")


# -----------------------------------------------------------------------------
# 3. contextlib.suppress - Ignore specific exceptions
# -----------------------------------------------------------------------------


def remove_file_if_exists(filepath: str) -> None:
    """
    Remove file. Suppress FileNotFoundError (file may not exist).
    """
    with suppress(FileNotFoundError):
        os.remove(filepath)
        print(f"Removed: {filepath}")


def parse_int_safe(value: str, default: int = 0) -> int:
    """
    Convert string to int. Use suppress to avoid try/except for simple case.
    """
    with suppress(ValueError):
        return int(value)
    return default


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 55)
    print("1. read_file_safe - File not found")
    print("=" * 55)
    read_file_safe("nonexistent_file_12345.txt")

    print("\n" + "=" * 55)
    print("2. read_file_safe - Valid file (this script)")
    print("=" * 55)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_file_safe(__file__)
    if content:
        lines = content.strip().split("\n")[:5]
        print("First 5 lines of this script:")
        for line in lines:
            print(f"  {line}")

    print("\n" + "=" * 55)
    print("3. write_file_safe + read - Temp file")
    print("=" * 55)
    demo_nested_context()

    print("\n" + "=" * 55)
    print("4. suppress(FileNotFoundError) - Remove nonexistent file")
    print("=" * 55)
    remove_file_if_exists("nonexistent_12345.txt")
    print("(No error raised)")

    print("\n" + "=" * 55)
    print("5. parse_int_safe with suppress")
    print("=" * 55)
    for val in ("42", "abc", "-7"):
        result = parse_int_safe(val, default=-1)
        print(f"  parse_int_safe({val!r}, default=-1) -> {result}")
