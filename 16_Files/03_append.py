"""
16_Files - Exercise 03: Append content to the end
=================================================
open() with mode "a" opens for appending; it does not erase existing content.
"""

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
