# -------------------------------------------------
# File Name: 027_split_list_into_variables.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Split List into Different Variables
# -------------------------------------------------

lst = [1, 2, 3, 4]
a, b, c, d = lst
print(a, b, c, d)  # 1 2 3 4

# Or with * for rest
first, *rest = lst
print(first, rest)  # 1 [2, 3, 4]
