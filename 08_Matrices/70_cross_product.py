# -------------------------------------------------
# File Name: 70_cross_product.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: np.cross(a, b) gives vector perpendicular to both.
# -------------------------------------------------

import numpy as np

a = np.array([1, 0, 0])
b = np.array([0, 1, 0])
c = np.cross(a, b)
print("a:", a)
print("b:", b)
print("a x b:", c)
print("Dot a·c:", np.dot(a, c))
print("Dot b·c:", np.dot(b, c))
