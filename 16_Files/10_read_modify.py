"""
16_Files - Exercise 10: Read file, modify content, write back
=============================================================
Read all lines, modify one or more, write back with writelines().
"""

# 1. Read all lines
with open("students.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 2. Modify one student (e.g. Bob: change GPA from 2.9 to 3.5)
for i, line in enumerate(lines):
    if line.strip().startswith("Bob,"):
        lines[i] = "Bob,Math,3.5\n"
        break

# 3. Write back to file
with open("students.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

# 4. Print file after modification
print("Students after modification:")
with open("students.txt", "r", encoding="utf-8") as f:
    print(f.read())
print("Bob's GPA updated: 2.9 -> 3.5")
