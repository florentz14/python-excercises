# 77. Decode Run-Length Encoded List

def decode_rle(encoded: list) -> list:
    result = []
    for x in encoded:
        if isinstance(x, list):
            count, val = x[0], x[1]
            result.extend([val] * count)
        else:
            result.append(x)
    return result


print(decode_rle([[2, 1], 2, 3, [2, 4], 5, 1]))  # [1, 1, 2, 3, 4, 4, 5, 1]
