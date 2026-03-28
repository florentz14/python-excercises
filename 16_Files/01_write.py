# -------------------------------------------------
# File Name: 01_write.py
# Created: 2026-03-06
# Author: Florentino Báez
# Date: 2026-03-06
# Description: Create and write to a file. open() with mode 'w' creates/overwrites. write() and writelines().
# -------------------------------------------------

filename = "example_01.txt"
content = "Hello, this is the file content.\nSecond line.\n"

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print(f"File '{filename}' created and written successfully.")

# Alternative: writelines() for a list of lines
lines = ["Line A\n", "Line B\n", "Line C\n"]
with open("example_01_lines.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("File 'example_01_lines.txt' created with writelines().")

# Create students.txt for subsequent examples (04_read_lines, 10_read_modify)
with open("students.txt", "w", encoding="utf-8") as f:
    f.write("Ana,CS,3.8\n")
    f.write("Bob,Math,2.9\n")
    f.write("Carol,Engineering,3.5")
print("File 'students.txt' created (for read_lines and read_modify examples).")
