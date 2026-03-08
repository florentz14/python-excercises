# -------------------------------------------------
# File Name: 39_group_ab.py
# Description: Group A/B by sex and name (A: women before M, men after N)
# -------------------------------------------------

name = input("Enter your name: ").strip()
sex = input("Enter sex (M/F): ").strip().upper()

first = name[0].upper() if name else ""
if sex == "F":
    in_group_a = first < "M"
elif sex == "M":
    in_group_a = first > "N"
else:
    in_group_a = False

print("Group A" if in_group_a else "Group B")
