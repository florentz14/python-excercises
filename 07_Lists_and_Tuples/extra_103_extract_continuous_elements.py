# 103. Extract N Elements That Follow Each Other Continuously (same value repeated n times)

def extract_continuous(lst: list, n: int) -> list:
    """Find values that appear n times in a row."""
    result = []
    i = 0
    while i <= len(lst) - n:
        if all(lst[i] == lst[i + j] for j in range(n)):
            result.append(lst[i])
            i += n
        else:
            i += 1
    return result


print(extract_continuous([1, 1, 3, 4, 4, 5, 6, 7], 2))  # [1, 4]
