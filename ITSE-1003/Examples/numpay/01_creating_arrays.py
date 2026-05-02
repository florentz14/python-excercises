import numpy as np

print("=" * 50)
print("1. CREATING ARRAYS")
print("=" * 50)

a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([[1, 2, 3], [4, 5, 6]])
a3 = np.zeros((3, 3))
a4 = np.ones((2, 4))
a5 = np.arange(0, 20, 2)
a6 = np.linspace(0, 1, 5)

print(f"1D array:        {a1}")
print(f"2D array:\n{a2}")
print(f"Zeros (3x3):\n{a3}")
print(f"Ones  (2x4):\n{a4}")
print(f"Arange(0,20,2):  {a5}")
print(f"Linspace(0,1,5): {a6}")
