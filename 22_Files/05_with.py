# 05_with.py - Write using 'with' (closes automatically)
# Florentino Baez - ITSE-1002

# with closes the file automatically
with open("students.txt", "w") as f:
    f.write("Ana,CS,3.8\n")
    f.write("Bob,Math,2.9\n")
    f.write("Carol,Engineering,3.5")
print("Done. File closed automatically.")
