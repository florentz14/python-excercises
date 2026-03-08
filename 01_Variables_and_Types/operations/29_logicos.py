# -------------------------------------------------
# File Name: 29_logicos.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Spanish-focused demo of logical operators (and, or, not)
# -------------------------------------------------

p = True
q = False
print("p =", p, ", q =", q)
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

# Practical application: verify combined conditions
age = 25
has_license = True
can_drive = age >= 18 and has_license
print("\nAge:", age, ", License:", has_license)
print("Can drive:", can_drive)
