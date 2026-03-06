"""
16_Files - Exercise 04: Read line by line
=========================================
Use readlines() or iterate directly over the file object.
"""

# Read each line with readlines()
with open("students.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    print(f"{i}: {line}", end="")

# Alternative: iterate directly (memory efficient for large files)
print("\n--- Direct iteration ---")
with open("students.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}: {line.rstrip()}")
