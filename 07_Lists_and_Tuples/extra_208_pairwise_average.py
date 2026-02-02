# 208. Pairwise Average: (a[i]+a[i+1])/2 for each i

def pairwise_average(lst: list[float]) -> list[float]:
    return [(lst[i] + lst[i + 1]) / 2 for i in range(len(lst) - 1)]


print(pairwise_average([1, 2, 3, 4, 5, 6, 7]))  # [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
print(pairwise_average([0, 1, -3, 3, 7, -5, 6, 7, 11]))
