# -------------------------------------------------
# File Name: 06_list_directory.py
# Author: Florentino Báez
# Date: 16_Files
# Description: List directory contents. os.listdir() and os.scandir().
# -------------------------------------------------

import os
from pathlib import Path

# Directory path (where this script is located)
directory = Path(__file__).parent

# With pathlib
print("--- Directory contents (pathlib) ---")
for item in directory.iterdir():
    item_type = "folder" if item.is_dir() else "file"
    print(f"  {item_type}: {item.name}")

# With os.listdir()
print("\n--- Directory contents (os.listdir) ---")
for name in os.listdir(directory):
    path = directory / name
    item_type = "folder" if path.is_dir() else "file"
    print(f"  {item_type}: {name}")

# Only .py files
print("\n--- Only .py files ---")
for f in directory.glob("*.py"):
    print(f"  {f.name}")
