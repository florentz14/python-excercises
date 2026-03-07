# ------------------------------------------------------------
# File: 21_sort_list_of_tuples.py
# Purpose: Sort list of tuples.
# Description: sort() with key=lambda for custom ordering.
# ------------------------------------------------------------

students = [
    ("Anna", 90),
    ("Louis", 85),
    ("Carlos", 95),
]
print("Original:", students)

# Sort by score (index 1)
by_score = sorted(students, key=lambda x: x[1])
print("By score:", by_score)

# Sort by name (index 0)
by_name = sorted(students, key=lambda x: x[0])
print("By name:", by_name)
