# 04_read_lines.py - Read line by line
# Florentino Baez - ITSE-1002

# Read each line
f = open("students.txt", "r")
lines = f.readlines()
f.close()
for i, line in enumerate(lines, 1):
    print(f"{i}: {line}", end="")
