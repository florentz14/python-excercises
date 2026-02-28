# 01_write.py - Write to a file (overwrites if exists)
# Florentino Baez - ITSE-1002

# Create/overwrite file with student list
f = open("students.txt", "w")
f.write("Ana,CS,3.8\n")
f.write("Bob,Math,2.9\n")
f.write("Carol,Engineering,3.5")
f.close()
print("File written: students.txt")
