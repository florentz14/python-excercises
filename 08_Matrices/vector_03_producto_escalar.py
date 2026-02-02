"""
Vectores - Ejemplo 3: Producto por escalar
==========================================
Tema: Vectores (08_Matrices)
Descripción: Multiplicar un vector por un número (escalar).
"""

v = [2, -3, 5]
k = 3

# k * v = (k*v[0], k*v[1], k*v[2])
resultado = [k * x for x in v]
print("v =", v)
print("k =", k)
print("k * v =", resultado)
