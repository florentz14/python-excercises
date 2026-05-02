import numpy as np

print("=" * 50)
print("3. ARRAY SLICING")
print("=" * 50)

arr = np.array([10, 20, 30, 40, 50, 60, 70])
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9,10,11,12]])

print(f"Array:             {arr}")
print(f"arr[1:4]:          {arr[1:4]}")
print(f"arr[:3]:           {arr[:3]}")
print(f"arr[4:]:           {arr[4:]}")
print(f"arr[::2]:          {arr[::2]}")
print(f"Matrix rows 0-1, cols 1-3:\n{matrix[0:2, 1:3]}")
