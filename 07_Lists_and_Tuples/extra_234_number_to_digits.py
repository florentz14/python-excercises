# 234. Convert Number to List of Digits

def number_to_digits(n: int) -> list[int]:
    return [int(d) for d in str(abs(n))]


print(number_to_digits(123))      # [1, 2, 3]
print(number_to_digits(1347823)) # [1, 3, 4, 7, 8, 2, 3]
