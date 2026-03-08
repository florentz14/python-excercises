# -------------------------------------------------
# File Name: 103_triangle_odd_numbers.py
# Description: Right triangle of odd numbers (1, 3 1, 5 3 1, ...)
# -------------------------------------------------

n = int(input("Enter height: "))
for i in range(n):
    row = list(range(2 * i + 1, 0, -2))
    print(" ".join(str(x) for x in row))
