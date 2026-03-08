# -------------------------------------------------
# File Name: 050_modified_run_length_encode.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Modified Run-Length Encode: single items not in [count, value]
# -------------------------------------------------

def modified_rle(lst: list) -> list:
    if not lst:
        return []
    result = []
    count = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            count += 1
        else:
            # Si count > 1: añadir [cantidad, valor]; si no, solo el valor (sin envolver en lista)
            result.append([count, lst[i - 1]] if count > 1 else lst[i - 1])
            count = 1
    # Última racha: mismo criterio (lista [n, x] solo si se repitió más de una vez)
    result.append([count, lst[-1]] if count > 1 else lst[-1])
    return result


print(modified_rle([1, 1, 2, 3, 4, 4, 5, 1]))
