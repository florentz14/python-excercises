# 209. Count Groups of Non-Zero Numbers Separated by Zeros

def count_nonzero_groups(lst: list[int]) -> int:
    count = 0
    in_group = False
    for x in lst:
        if x != 0:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False
    return count


sample = [3, 4, 6, 2, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 5, 9, 9, 7]
print(count_nonzero_groups(sample))
