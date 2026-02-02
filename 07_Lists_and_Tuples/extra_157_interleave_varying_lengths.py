# 157. Interleave Lists of Varying Lengths (cycle through until all exhausted)

def interleave_varying(*lists: list) -> list:
    result = []
    iters = [iter(L) for L in lists]
    active = list(range(len(lists)))
    while active:
        for i in list(active):
            try:
                result.append(next(iters[i]))
            except StopIteration:
                active.remove(i)
    return result


print(interleave_varying([2, 4, 7, 0, 5, 8], [2, 5, 8], [0, 1], [3, 3, -1, 7]))
