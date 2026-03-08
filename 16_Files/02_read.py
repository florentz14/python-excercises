# -------------------------------------------------
# File Name: 02_read.py
# Author: Florentino Báez
# Date: 16_Files
# Description: Read a file. open() with mode 'r'. read(), readline(), and iteration over lines.
# -------------------------------------------------

filename = "example_01.txt"

# Read entire content at once
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

print("--- read() (whole file) ---")
print(content)

# Read line by line (useful for large files)
print("\n--- readline() / iterate ---")
with open(filename, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"Line {i}: {line.rstrip()}")

# Read all lines as a list
with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
print("\n--- readlines() ---")
print(lines)
