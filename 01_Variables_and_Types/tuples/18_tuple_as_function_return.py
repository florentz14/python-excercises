# ------------------------------------------------------------
# File: 18_tuple_as_function_return.py
# Purpose: Tuples as function return values.
# Description: Return multiple values from a function.
# ------------------------------------------------------------

def min_max(nums):
    return min(nums), max(nums)

values = [1, 5, 3, 9, 2]
lo, hi = min_max(values)
print("min_max([1,5,3,9,2]):", lo, hi)

# Return as single tuple
result = min_max(values)
print("result:", result, "type:", type(result))
