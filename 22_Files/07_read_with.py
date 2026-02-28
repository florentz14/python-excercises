# 07_read_with.py - Read file using 'with'
# Florentino Baez - ITSE-1002

# with closes the file automatically
with open("students.txt", "r") as f:
    content = f.read()

print("Students:")
print(content)
print("Done. File closed automatically.")
