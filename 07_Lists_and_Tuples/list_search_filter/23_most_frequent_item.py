# -------------------------------------------------
# File Name: 23_most_frequent_item.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Find Item with Most Occurrences in List
# -------------------------------------------------

from collections import Counter

def most_frequent(lst: list):
    # Se devuelve un valor u otro según la condición.
    return Counter(lst).most_common(1)[0][0] if lst else None


sample = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
print(most_frequent(sample))  # 2
