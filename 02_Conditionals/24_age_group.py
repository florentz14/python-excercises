# -------------------------------------------------
# File Name: 24_age_group.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Age group classifier
# -------------------------------------------------

age = int(input("Enter your age: "))

if age < 13:
    group = "child"
elif age < 20:
    group = "teen"
elif age < 65:
    group = "adult"
else:
    group = "senior"

print(f"Age {age} → {group}")
