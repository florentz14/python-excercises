# -------------------------------------------------
# File Name: 36_for_continue.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: continue statement.
# -------------------------------------------------

for i in range(1, 6):
    if i == 3:
        print("Skipping 3")
        continue
    print(i)
