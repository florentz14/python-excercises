# -------------------------------------------------
# File Name: 65_magnitude.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: ||v|| = sqrt(v[0]² + v[1]² + ...).
# -------------------------------------------------

import math

v = [3, 4]  # In R², ||v|| = 5

# Magnitude: square root of sum of squares
magnitude = math.sqrt(sum(x * x for x in v))
print("v =", v)
print("||v|| =", magnitude)

# Unit vector example
u = [1, 0, 0]
print("\nu =", u)
print("||u|| =", math.sqrt(sum(x * x for x in u)))
