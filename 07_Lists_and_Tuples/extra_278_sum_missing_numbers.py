# 278. Sum of Missing Numbers (in range min to max not in list)

def sum_missing(lst: list[int]) -> int:
    if not lst:
        return 0
    mn, mx = min(lst), max(lst)
    present = set(lst)
    return sum(x for x in range(mn, mx + 1) if x not in present)


print(sum_missing([0, 3, 4, 7, 9]))   # 1+2+5+6+8 = 22
print(sum_missing([44, 45, 48]))      # 46+47 = 93
print(sum_missing([-7, -5, -4, 0]))  # -6+-3+-2+-1 = -12
