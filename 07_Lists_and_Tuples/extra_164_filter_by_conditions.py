# 164. Get Items from List with Specific Conditions (e.g. even and > 45)

def filter_by_conditions(lst: list[int], *conditions) -> list[int]:
    result = lst
    for cond in conditions:
        result = [x for x in result if cond(x)]
    return result


sample = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
even_gt_45 = [x for x in sample if x % 2 == 0 and x > 45]
print("Even and > 45:", even_gt_45)
print("Count:", len(even_gt_45))
