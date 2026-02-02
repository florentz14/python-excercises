# 131. Frequency of Consecutive Duplicate Elements (unique values + their run counts)

def consecutive_frequency(lst: list) -> tuple[list, list]:
    if not lst:
        return [], []
    values, counts = [lst[0]], [1]
    for x in lst[1:]:
        if x == values[-1]:
            counts[-1] += 1
        else:
            values.append(x)
            counts.append(1)
    return values, counts


sample = [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
print(consecutive_frequency(sample))  # ([1, 2, 4, 5], [1, 3, 3, 4])
