import numpy as np

print("=" * 50)
print("7. ARRAY RESHAPE")
print("=" * 50)

arr = np.arange(1, 13)
print(f"Original (12,):  {arr}")

r1 = arr.reshape(3, 4)
print(f"Reshaped (3,4):\n{r1}")

r2 = arr.reshape(2, 3, 2)
print(f"Reshaped (2,3,2):\n{r2}")

r3 = arr.reshape(4, -1)   # -1 = NumPy calcula automáticamente
print(f"Reshaped (4,-1):\n{r3}")

flat = r1.flatten()
print(f"Flattened: {flat}")
