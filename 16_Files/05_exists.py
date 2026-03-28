# -------------------------------------------------
# File Name: 05_exists.py
# Created: 2026-03-06
# Author: Florentino Báez
# Date: 2026-03-06
# Description: Check if file exists. os.path.exists() and pathlib.Path.exists().
# -------------------------------------------------

from pathlib import Path

# Check if exists (file or folder)
file_path = Path("example_01.txt")
folder_path = Path(__file__).parent

if file_path.exists():
    print(f"'{file_path}' exists.")
else:
    print(f"'{file_path}' does not exist.")

# Differentiate file and folder
if file_path.is_file():
    print("  -> It is a file.")
if file_path.is_dir():
    print("  -> It is a directory.")

if folder_path.exists() and folder_path.is_dir():
    print(f"\n'{folder_path.name}' is an existing directory.")

# Check before reading (avoid FileNotFoundError)
file_to_read = Path("example_01.txt")
if file_to_read.is_file():
    print(f"\nWe can safely read '{file_to_read}'.")
else:
    print(f"\nCannot read: '{file_to_read}' is not a file or does not exist.")
