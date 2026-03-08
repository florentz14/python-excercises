# -------------------------------------------------
# File Name: 13_multiplication_table.py
# Author: Florentino Báez
# Date: 04_Functions
# Description: Display multiplication table for a number.
# -------------------------------------------------

def multiplication_table(num: int) -> None:
    for i in range(1, 6):
        print(num, "x", i, "=", num * i)


multiplication_table(3)
