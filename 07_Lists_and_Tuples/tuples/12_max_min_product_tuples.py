# -------------------------------------------------
# File Name: 12_max_min_product_tuples.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Max and Min Product of Tuple Pairs (a*b for each (a,b))
# -------------------------------------------------

def max_min_product(tuples: list[tuple[int, int]]) -> tuple[int, int]:
    products = [a * b for a, b in tuples]
    return max(products), min(products)


sample = [(2, 7), (2, 6), (1, 8), (4, 9)]
print(max_min_product(sample))  # (36, 8)
