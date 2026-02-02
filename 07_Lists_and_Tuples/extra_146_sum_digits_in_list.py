# 146. Sum of Digits of Each Number in List (ignore non-numeric)

def sum_digits(n: int) -> int:
    return sum(int(d) for d in str(abs(n)) if d.isdigit())


def sum_digits_list(lst: list) -> int:
    return sum(sum_digits(x) for x in lst if isinstance(x, (int, float)) and not isinstance(x, bool))


print(sum_digits_list([10, 2, 56]))           # 1+0 + 2 + 5+6 = 14
print(sum_digits_list([10, 20, -4, 5, -70]))  # 19
