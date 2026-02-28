# 08_read_for_enumerate.py - Read file using for with enumerate
# Florentino Baez - ITSE-1002

with open("students.txt", "r") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}: {line}", end="")

print("\nDone.")
