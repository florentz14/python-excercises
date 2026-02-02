# 75. Run-Length Encoding - [[count, value], ...]

def run_length_encode(lst: list) -> list[list]:
    if not lst:
        return []
    result = []
    count = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            count += 1
        else:
            result.append([count, lst[i - 1]])
            count = 1
    result.append([count, lst[-1]])
    return result


print(run_length_encode([1, 1, 2, 3, 4, 4, 5, 1]))
