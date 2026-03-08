# -------------------------------------------------
# File Name: 20_recursive_directory_walk.py
# Author: Florentino Báez
# Date: 16_Files
# Description: Recursive directory walk. os.walk() for traversing directory trees.
# -------------------------------------------------

import os
import shutil

# Create a directory structure for demonstration
base_dir = "walk_example"
os.makedirs(os.path.join(base_dir, "subdir1"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "subdir2", "nested"), exist_ok=True)

# Create some files
files_to_create = [
    os.path.join(base_dir, "file1.txt"),
    os.path.join(base_dir, "subdir1", "file2.txt"),
    os.path.join(base_dir, "subdir1", "file3.py"),
    os.path.join(base_dir, "subdir2", "file4.txt"),
    os.path.join(base_dir, "subdir2", "nested", "file5.txt")
]

for file_path in files_to_create:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"Content of {os.path.basename(file_path)}\n")

print(f"Created directory structure in '{base_dir}'.")

# Walk through the directory tree
print("\nWalking through directory tree:")
for root, dirs, files in os.walk(base_dir):
    level = root.replace(base_dir, '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f"{subindent}{file}")

# Find all .txt files
print("\nFinding all .txt files:")
txt_files = []
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.txt'):
            txt_files.append(os.path.join(root, file))

for txt_file in txt_files:
    print(f"  {txt_file}")

# Count files by extension
print("\nFile count by extension:")
extension_count = {}
for root, dirs, files in os.walk(base_dir):
    for file in files:
        ext = os.path.splitext(file)[1]
        extension_count[ext] = extension_count.get(ext, 0) + 1

for ext, count in extension_count.items():
    print(f"  {ext or 'no extension'}: {count}")

# Calculate total size
total_size = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        file_path = os.path.join(root, file)
        total_size += os.path.getsize(file_path)

print(f"\nTotal size of all files: {total_size} bytes")

# Clean up
shutil.rmtree(base_dir)
print(f"Removed directory structure '{base_dir}'.")
