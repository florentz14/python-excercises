# -------------------------------------------------
# File Name: 29_comp_from_lists.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Build dict from two lists using zip() in comprehension.
# -------------------------------------------------

print("3. Creating Dictionary from Two Lists:")
print("-" * 60)
names = ["Alice", "Bob", "Charlie", "Diana"]
scores = [85, 92, 78, 95]
# zip() creates pairs: (name, score), unpacked in the comprehension
student_scores = {name: score for name, score in zip(names, scores)}
print(f"Student scores: {student_scores}")
