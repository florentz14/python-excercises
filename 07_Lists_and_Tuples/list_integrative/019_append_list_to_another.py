# -------------------------------------------------
# File Name: 019_append_list_to_another.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Append a List to Another List
# -------------------------------------------------

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)  # or a += b
print(a)  # [1, 2, 3, 4, 5, 6]
