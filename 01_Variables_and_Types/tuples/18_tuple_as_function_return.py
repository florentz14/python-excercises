# -------------------------------------------------
# File Name: 18_tuple_as_function_return.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Tuples as function return values.
# -------------------------------------------------

def min_max(nums):
    return min(nums), max(nums)

values = [1, 5, 3, 9, 2]
lo, hi = min_max(values)
print("min_max([1,5,3,9,2]):", lo, hi)

# Return as single tuple
result = min_max(values)
print("result:", result, "type:", type(result))
