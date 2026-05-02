import numpy as np

print("=" * 50)
print("9. ARRAY JOIN")
print("=" * 50)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

concat  = np.concatenate((a, b))
vstack  = np.vstack((a, b))
hstack  = np.hstack((a, b))

a2 = np.array([[1, 2], [3, 4]])
b2 = np.array([[5, 6], [7, 8]])
axis0 = np.concatenate((a2, b2), axis=0)
axis1 = np.concatenate((a2, b2), axis=1)

print(f"concatenate:    {concat}")
print(f"vstack:\n{vstack}")
print(f"hstack:         {hstack}")
print(f"concat axis=0:\n{axis0}")
print(f"concat axis=1:\n{axis1}")
