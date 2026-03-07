"""
16_Files - Exercise 19: Modern file handling with pathlib
========================================================
pathlib provides an object-oriented interface to filesystem paths.
It's more intuitive and cross-platform than os.path.
"""

from pathlib import Path
import shutil

# Create Path objects
current_dir = Path(".")
data_file = Path("pathlib_data.txt")
subdir = Path("example_dir")
nested_file = subdir / "nested.txt"

print(f"Current directory: {current_dir.absolute()}")

# Create and write to a file
data_file.write_text(
    "Hello from pathlib!\nThis is modern Python file handling.")
print(f"Created file: {data_file}")

# Read the file
content = data_file.read_text()
print(f"File content: {content}")

# Check file properties
print(f"File exists: {data_file.exists()}")
print(f"Is file: {data_file.is_file()}")
print(f"File size: {data_file.stat().st_size} bytes")
print(f"File extension: {data_file.suffix}")

# Create directory
subdir.mkdir(exist_ok=True)
print(f"Created directory: {subdir}")

# Create nested file
nested_file.write_text("Content in nested file.")
print(f"Created nested file: {nested_file}")

# List directory contents
print(f"\nContents of {subdir}:")
for item in subdir.iterdir():
    print(f"  {item.name} ({'file' if item.is_file() else 'dir'})")

# Path operations
print(f"\nPath operations:")
print(f"Parent: {data_file.parent}")
print(f"Name: {data_file.name}")
print(f"Stem: {data_file.stem}")
print(f"With suffix .bak: {data_file.with_suffix('.bak')}")

# Glob patterns
print(f"\nFiles matching *.txt:")
for txt_file in current_dir.glob("*.txt"):
    print(f"  {txt_file.name}")

# Recursive glob
print(f"\nAll .txt files recursively:")
for txt_file in current_dir.rglob("*.txt"):
    print(f"  {txt_file}")

# Copy and move with pathlib
backup_file = data_file.with_suffix('.bak')
shutil.copy(data_file, backup_file)
print(f"\nCopied to: {backup_file}")

# Clean up
backup_file.unlink()
nested_file.unlink()
subdir.rmdir()
data_file.unlink()
print("Cleaned up files and directories.")
