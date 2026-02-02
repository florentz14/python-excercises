# 78. Split List into Two Parts by Length (first part has given length)

def split_by_length(lst: list, n: int) -> tuple[list, list]:
    return lst[:n], lst[n:]


sample = [1, 1, 2, 3, 4, 4, 5, 1]
print(split_by_length(sample, 3))  # ([1, 1, 2], [3, 4, 4, 5, 1])
