import numpy as np

print("=" * 50)
print("6. ARRAY SHAPE")
print("=" * 50)

a1 = np.array([1, 2, 3, 4])
a2 = np.array([[1, 2], [3, 4], [5, 6]])
a3 = np.zeros((2, 3, 4))

print(f"1D shape: {a1.shape}       ndim={a1.ndim}  size={a1.size}")
print(f"2D shape: {a2.shape}      ndim={a2.ndim}  size={a2.size}")
print(f"3D shape: {a3.shape}  ndim={a3.ndim}  size={a3.size}")
