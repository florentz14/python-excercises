# -------------------------------------------------
# File Name: 41_employee_performance.py
# Description: Performance level and bonus (0.0, 0.4, 0.6 or more)
# -------------------------------------------------

BASE = 2400
score = float(input("Enter performance score (0.0, 0.4, 0.6+): "))

if score == 0.0:
    level = "Unacceptable"
elif score == 0.4:
    level = "Acceptable"
elif score >= 0.6:
    level = "Meritorious"
else:
    level = "Invalid score"
    score = 0

if level != "Invalid score":
    bonus = BASE * score
    print(f"Level: {level}")
    print(f"Bonus: {bonus:.0f} EUR")
else:
    print(level)
