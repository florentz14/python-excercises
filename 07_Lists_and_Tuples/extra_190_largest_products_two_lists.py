# 190. N Largest Products from Two Lists (one from each list)

def n_largest_products(a: list[int], b: list[int], n: int) -> list[int]:
    products = [x * y for x in a for y in b]
    return sorted(products, reverse=True)[:n]


list1 = [1, 2, 3, 4, 5, 6]
list2 = [3, 6, 8, 9, 10, 6]
print(n_largest_products(list1, list2, 3))  # [60, 54, 50]
print(n_largest_products(list1, list2, 4))  # [60, 54, 50, 48]
