# -------------------------------------------------
# File Name: 09_with_context.py
# Created: 2026-03-06
# Author: Florentino Báez
# Date: 2026-03-06
# Description: Using with for file operations. Context manager ensures proper closing.
# -------------------------------------------------

name = "example_09_with.txt"
with open(name, "w", encoding="utf-8") as f:
    f.write("Written inside the with block.\n")
    # No need for f.close()
# File is already closed here

print(f"File '{name}' written and closed successfully.")

# Read with with
with open(name, "r", encoding="utf-8") as f:
    text = f.read()
    print("Read content:")
    print(text)

# Multiple files in the same with (Python 3.10+)
with (
    open("example_09_a.txt", "w", encoding="utf-8") as a,
    open("example_09_b.txt", "w", encoding="utf-8") as b,
):
    a.write("File A\n")
    b.write("File B\n")
print("Files A and B created with a single with.")
