import numpy as np

print("=" * 50)
print("5. COPY VS VIEW")
print("=" * 50)

original = np.array([1, 2, 3, 4, 5])

view = original.view()
view[0] = 99
print(f"After modifying VIEW[0]=99:")
print(f"  original: {original}")   # también cambia
print(f"  view:     {view}")

original2 = np.array([1, 2, 3, 4, 5])
copy = original2.copy()
copy[0] = 99
print(f"After modifying COPY[0]=99:")
print(f"  original2: {original2}")  # no cambia
print(f"  copy:      {copy}")

print(f"view.base is original  → {view.base is original}")
print(f"copy.base is None      → {copy.base is None}")
