# 233. Chunk List into n Smaller Lists (as equal as possible)

def chunk_into_n(lst: list, n: int) -> list[list]:
    size = len(lst)
    base, extra = divmod(size, n)
    result = []
    start = 0
    for i in range(n):
        length = base + (1 if i < extra else 0)
        result.append(lst[start:start + length])
        start += length
    return result


print(chunk_into_n([1, 2, 3, 4, 5, 6, 7], 4))  # [[1,2], [3,4], [5,6], [7]]
