# -------------------------------------------------
# File Name: 67_unit_vector.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: u = v / ||v|| has magnitude 1.
# -------------------------------------------------

import numpy as np

v = np.array([3, 4])
magnitude = np.linalg.norm(v)
u = v / magnitude
print("Vector v:", v)
print("Magnitude ||v||:", magnitude)
print("Unit vector u = v/||v||:", u)
print("||u||:", np.linalg.norm(u))
