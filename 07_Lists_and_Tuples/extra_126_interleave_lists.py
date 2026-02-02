# 126. Interleave Multiple Lists (same length): [1,2,3], [10,20,30], [100,200,300] -> [1,10,100,2,20,200,...]

def interleave(*lists: list) -> list:
    return [x for t in zip(*lists) for x in t]


list1, list2, list3 = [1, 2, 3, 4, 5, 6, 7], [10, 20, 30, 40, 50, 60, 70], [100, 200, 300, 400, 500, 600, 700]
print(interleave(list1, list2, list3))
