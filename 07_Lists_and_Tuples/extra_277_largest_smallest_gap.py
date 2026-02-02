# 277. Largest and Smallest Gap Between Sorted Elements

def largest_smallest_gap(lst: list[int]) -> tuple[int, int]:
    sorted_lst = sorted(lst)
    gaps = [sorted_lst[i + 1] - sorted_lst[i] for i in range(len(sorted_lst) - 1)]
    return max(gaps), min(gaps) if gaps else (0, 0)


print(largest_smallest_gap([1, 2, 9, 0, 4, 6]))  # max gap 5 (2 to 4? 4 to 6:2, 6 to 9:3, 1-2:1, 2-4:2, 4-6:2, 6-9:3. Sorted: 0,1,2,4,6,9 -> gaps 1,1,2,2,3 -> max 3 min 1)
# Actually sample says "largest and smallest gap" -> 3 and 1
print(largest_smallest_gap([1, 2, 9, 0, 4, 6]))
print(largest_smallest_gap([23, -2, 45, 38, 12, 4, 6]))
