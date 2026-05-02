import numpy as np

print("=" * 50)
print("10. ARRAY SPLIT")
print("=" * 50)

arr = np.array([1, 2, 3, 4, 5, 6])
s1 = np.array_split(arr, 3)          # 3 partes iguales
s2 = np.array_split(arr, [2, 4])     # split en índices 2 y 4

matrix = np.arange(1, 17).reshape(4, 4)
v = np.vsplit(matrix, 2)             # split vertical
h = np.hsplit(matrix, 2)             # split horizontal

print(f"Split en 3:        {s1}")
print(f"Split en [2,4]:    {s2}")
print(f"vsplit (2 bloques):\n{v[0]}\n---\n{v[1]}")
print(f"hsplit col 0:\n{h[0]}")
