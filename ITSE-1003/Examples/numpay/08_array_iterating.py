import numpy as np

print("=" * 50)
print("8. ARRAY ITERATING")
print("=" * 50)

arr1d = np.array([10, 20, 30])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

print("Iterate 1D:")
for x in arr1d:
    print(f"  {x}")

print("Iterate 2D (row by row):")
for row in arr2d:
    print(f"  {row}")

print("Iterate 2D element by element (nditer):")
for elem in np.nditer(arr2d):
    print(f"  {elem}", end=" ")
print()

print("ndindex (index + value):")
for idx in np.ndindex(arr2d.shape):
    print(f"  {idx} → {arr2d[idx]}")
