# 09_read_modify.py - Read students file and modify one student
# Florentino Baez - ITSE-1002

# 1. Read all lines
with open("students.txt", "r") as f:
    lines = f.readlines()

# 2. Modify one student (Bob: change GPA from 2.9 to 3.5)
for i, line in enumerate(lines):
    if line.strip().startswith("Bob,"):
        lines[i] = "Bob,Math,3.5\n"
        break

# 3. Write back to file
with open("students.txt", "w") as f:
    f.writelines(lines)

# 4. Print the file after modification
print("Students after modification:")
with open("students.txt", "r") as f:
    print(f.read())
print("Bob's GPA updated: 2.9 -> 3.5")
