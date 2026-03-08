# -------------------------------------------------
# File Name: 03_file_exceptions.py
# Author: Florentino Báez
# Date: 22_Exceptions
# Description: File Exceptions - FileNotFoundError, PermissionError, IOError ============================================================= Common exceptions when working with files:
# -------------------------------------------------

import os


# =============================================================================
# 1. FileNotFoundError - File does not exist
# =============================================================================

def read_file_safe(path: str) -> str | None:
    """Read file contents. Returns None if file not found."""
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None


# =============================================================================
# 2. Multiple file exceptions
# =============================================================================

def read_file_robust(path: str) -> str | None:
    """Read file. Handles FileNotFoundError, PermissionError, UnicodeDecodeError."""
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{path}' does not exist.")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{path}'.")
        return None
    except UnicodeDecodeError as e:
        print(f"Error: Cannot decode file (wrong encoding?): {e}")
        return None


# =============================================================================
# 3. Check file exists before opening
# =============================================================================

def read_file_if_exists(path: str) -> str | None:
    """Read file only if it exists. Raises FileNotFoundError otherwise."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, encoding="utf-8") as f:
        return f.read()


# =============================================================================
# 4. Write to file - PermissionError (read-only filesystem)
# =============================================================================

def write_to_file(path: str, content: str) -> bool:
    """Write content to file. Returns True on success, False on error."""
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully wrote to {path}")
        return True
    except PermissionError:
        print(f"Error: No permission to write to '{path}'.")
        return False
    except OSError as e:
        print(f"Error: I/O error - {e}")
        return False


# =============================================================================
# Main - Run examples
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("1. FileNotFoundError - Read non-existent file")
    print("=" * 55)
    result = read_file_safe("nonexistent_file_12345.txt")
    if result is None:
        print("(Handled: returned None)")

    print("\n" + "=" * 55)
    print("2. Read existing file (this script)")
    print("=" * 55)
    script_path = os.path.join(os.path.dirname(__file__), "03_file_exceptions.py")
    result = read_file_robust(script_path)
    if result:
        lines = result.strip().split("\n")
        print(f"Read {len(lines)} lines. First line: {lines[0][:50]}...")

    print("\n" + "=" * 55)
    print("3. read_file_if_exists - Raise FileNotFoundError")
    print("=" * 55)
    try:
        read_file_if_exists("another_missing_file.txt")
    except FileNotFoundError as e:
        print(f"Caught: {e}")

    print("\n" + "=" * 55)
    print("4. Write to file (temp file)")
    print("=" * 55)
    temp_path = os.path.join(os.path.dirname(__file__), "_temp_example.txt")
    write_to_file(temp_path, "Hello from 03_file_exceptions.py")
    if os.path.exists(temp_path):
        os.remove(temp_path)
        print("(Temp file cleaned up)")
