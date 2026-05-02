import numpy as np

print("=" * 50)
print("12. ARRAY SORT")
print("=" * 50)

arr      = np.array([40, 10, 50, 20, 30])
matrix   = np.array([[3, 1, 2], [9, 6, 7]])

s_asc    = np.sort(arr)
s_desc   = np.sort(arr)[::-1]
s_axis0  = np.sort(matrix, axis=0)  # por columna
s_axis1  = np.sort(matrix, axis=1)  # por fila
argsorted = np.argsort(arr)          # índices que ordenarían el array

print(f"Original:      {arr}")
print(f"Ascending:     {s_asc}")
print(f"Descending:    {s_desc}")
print(f"Argsort:       {argsorted}")
print(f"Matrix sort axis=0:\n{s_axis0}")
print(f"Matrix sort axis=1:\n{s_axis1}")
