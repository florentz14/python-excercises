# -------------------------------------------------
# File Name: 39_grouping.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Group values into dict of lists (e.g., by parity, word length).
# -------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

grouped = {'even': [], 'odd': []}
for num in numbers:
    if num % 2 == 0:
        grouped['even'].append(num)
    else:
        grouped['odd'].append(num)

print("Grouped by parity:", grouped)

# Using defaultdict for automatic list creation
from collections import defaultdict

grouped_auto = defaultdict(list)
for num in numbers:
    key = 'even' if num % 2 == 0 else 'odd'
    grouped_auto[key].append(num)

print("Grouped with defaultdict:", dict(grouped_auto))

# More complex grouping: by length of string
words = ['cat', 'dog', 'elephant', 'ant', 'bird', 'hippopotamus']
grouped_by_len = defaultdict(list)
for word in words:
    grouped_by_len[len(word)].append(word)

print("Grouped by word length:", dict(grouped_by_len))