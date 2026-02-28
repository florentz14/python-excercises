# 02_read.py - Read entire file content
# Florentino Baez - ITSE-1002

# Read full file
f = open("students.txt", "r")
content = f.read()
f.close()
print("Students:")
print(content)
