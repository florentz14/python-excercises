# -------------------------------------------------
# File Name: 03_append.py
# Author: Florentino Báez
# Date: 16_Files
# Description: Append content to a file. open() with mode 'a' preserves existing content.
# -------------------------------------------------

filename = "example_03_append.txt"

# Create initial file if it does not exist
with open(filename, "w", encoding="utf-8") as f:
    f.write("First line.\n")

# Append more content without erasing previous
with open(filename, "a", encoding="utf-8") as f:
    f.write("Line appended after.\n")
    f.write("Another line.\n")

print(f"Content appended to '{filename}'.")

# Display result
with open(filename, "r", encoding="utf-8") as f:
    print("\nCurrent content:")
    print(f.read())
