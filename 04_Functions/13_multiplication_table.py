# -------------------------------------------------
# File: 13_multiplication_table.py
# Description: Display multiplication table for a number.
#              Function with loop (1 to 5).
# -------------------------------------------------

def multiplication_table(num: int) -> None:
    for i in range(1, 6):
        print(num, "x", i, "=", num * i)


multiplication_table(3)
