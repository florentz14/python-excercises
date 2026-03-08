# -------------------------------------------------
# File Name: 26_count_occurrences.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Counts element occurrences using list.count()
# -------------------------------------------------

from collections import Counter
numbers = [1, 2, 2, 3, 3, 3, 4]
print("Count of 2:", numbers.count(2))
print("Count of 3:", numbers.count(3))
print("Count of 5:", numbers.count(5))  # Not in list

# Using collections.Counter for all counts
print("All counts:", Counter(numbers))
