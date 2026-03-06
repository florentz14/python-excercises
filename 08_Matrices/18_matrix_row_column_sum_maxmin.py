# ------------------------------------------------------------
# File: 18_matrix_row_column_sum_maxmin.py
# Purpose: Row/column extraction, total sum, max/min.
# Description: Get row, get column, sum all elements, find max and min.
# ------------------------------------------------------------

M = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
]

print("Matrix:")
for row in M:
    print(row)

# Row 1 (0-based index)
print("Row 1:", M[1])

# Column 1: extract j-th element from each row
print("Column 1:", [row[1] for row in M])

# Sum of all elements
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nMatrix:", nums)
print("Total sum:", sum(sum(row) for row in nums))

# Max and min (flatten first)
flat = [x for row in nums for x in row]
print("Max:", max(flat))
print("Min:", min(flat))
