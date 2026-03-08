# -------------------------------------------------
# File Name: 06_remove_passed_subjects.py
# Description: Remove passed subjects, show subjects to repeat
# -------------------------------------------------

subjects = ["Mathematics", "Physics", "Chemistry", "History", "Language"]
to_repeat = []
for s in subjects:
    g = float(input(f"Grade in {s}: "))
    if g < 5:
        to_repeat.append(s)
print("Subjects to repeat:", to_repeat)
