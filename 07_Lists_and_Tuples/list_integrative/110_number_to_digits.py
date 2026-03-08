# -------------------------------------------------
# File Name: 110_number_to_digits.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Convert Number to List of Digits
# -------------------------------------------------

def number_to_digits(n: int) -> list[int]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [int(d) for d in str(abs(n))]


print(number_to_digits(123))      # [1, 2, 3]
print(number_to_digits(1347823)) # [1, 3, 4, 7, 8, 2, 3]
