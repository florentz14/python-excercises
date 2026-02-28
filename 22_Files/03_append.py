# 03_append.py - Append to end without erasing existing content
# Florentino Baez - ITSE-1002

# Append to file
f = open("students.txt", "a")
f.write("\nDave,Biology,3.2")
f.close()
print("Student appended to students.txt")
