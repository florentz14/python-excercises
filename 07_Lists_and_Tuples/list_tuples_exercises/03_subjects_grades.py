# -------------------------------------------------
# File Name: 03_subjects_grades.py
# Description: Ask grade for each subject, show "In <subject> you got <grade>"
# -------------------------------------------------

subjects = ["Mathematics", "Physics", "Chemistry", "History", "Language"]
grades = []
for s in subjects:
    g = input(f"Grade in {s}: ")
    grades.append(g)
for s, g in zip(subjects, grades):
    print(f"In {s} you got {g}")
