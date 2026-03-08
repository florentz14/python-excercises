# -------------------------------------------------
# File Name: 98_odd_numbers_comma.py
# Description: Odd numbers 1 to n, comma separated
# -------------------------------------------------

n = int(input("Enter a positive integer: "))
odds = [str(i) for i in range(1, n + 1, 2)]
print(", ".join(odds))
