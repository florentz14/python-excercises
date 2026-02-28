# 06_exists.py - Check if file exists
# Florentino Baez - ITSE-1002

from pathlib import Path

filepath = Path("students.txt")
if filepath.exists():
    print("The file exists")
else:
    print("The file does NOT exist")
