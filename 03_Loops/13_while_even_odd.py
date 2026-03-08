# -------------------------------------------------
# File Name: 13_while_even_odd.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Even/odd classification.
# -------------------------------------------------

count = 1

while count <= 10:
    if count % 2 == 0:
        print(count, "is even")
    else:
        print(count, "is odd")
    count = count + 1
