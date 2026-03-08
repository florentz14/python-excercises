# -------------------------------------------------
# File Name: 04_read_lines.py
# Author: Florentino Báez
# Date: 16_Files
# Description: Read file line by line. readlines() and iteration.
# -------------------------------------------------

with open("students.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    print(f"{i}: {line}", end="")

# Alternative: iterate directly (memory efficient for large files)
print("\n--- Direct iteration ---")
with open("students.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}: {line.rstrip()}")
