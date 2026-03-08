# -------------------------------------------------
# File Name: 11_scalar_product.py
# Description: Scalar product of (1,2,3) and (-1,0,2)
# -------------------------------------------------

v1 = [1, 2, 3]
v2 = [-1, 0, 2]
product = sum(a * b for a, b in zip(v1, v2))
print(product)
