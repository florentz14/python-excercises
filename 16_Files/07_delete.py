"""
16_Files - Exercise 07: Delete a file
=====================================
Path.unlink() or os.remove() delete the file (not folders).
"""

from pathlib import Path

# Create a test file to delete
test_file = Path("file_to_delete.txt")
test_file.write_text("Temporary content.\n", encoding="utf-8")
print(f"File '{test_file}' created.")

# Delete with pathlib
if test_file.exists():
    test_file.unlink()
    print(f"File '{test_file}' deleted with Path.unlink().")

# Alternative with os
import os
test_file2 = Path("file_to_delete_2.txt")
test_file2.write_text("Another temporary.\n", encoding="utf-8")
if test_file2.is_file():
    os.remove(test_file2)
    print(f"File '{test_file2}' deleted with os.remove().")

# Delete only if exists (avoid error)
path = Path("does_not_exist.txt")
if path.exists():
    path.unlink()
else:
    print("\n'does_not_exist.txt' does not exist; nothing to delete.")
