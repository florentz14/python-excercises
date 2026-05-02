import numpy as np

print("=" * 50)
print("2. ARRAY INDEXING")
print("=" * 50)

arr = np.array([10, 20, 30, 40, 50])
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(f"Array:            {arr}")
print(f"First element:    {arr[0]}")
print(f"Last element:     {arr[-1]}")
print(f"Matrix:\n{matrix}")
print(f"Row 1, Col 2:     {matrix[1, 2]}")
print(f"Last row:         {matrix[-1]}")
