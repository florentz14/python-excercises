import numpy as np

print("=" * 50)
print("11. ARRAY SEARCH")
print("=" * 50)

arr = np.array([10, 20, 30, 20, 40, 20, 50])

idx_where = np.where(arr == 20)
idx_gt30  = np.where(arr > 30)
idx_search = np.searchsorted(np.sort(arr), 25)  # búsqueda binaria

print(f"Array:                      {arr}")
print(f"where(arr == 20):           {idx_where[0]}")
print(f"where(arr > 30):            {idx_gt30[0]}")
print(f"searchsorted(sorted, 25):   index {idx_search}")
