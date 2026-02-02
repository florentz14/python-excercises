"""
Vectores - Ejemplo 4: Producto punto (producto escalar)
========================================================
Tema: Vectores (08_Matrices)
Descripción: v · w = v[0]*w[0] + v[1]*w[1] + ... (resultado es un número).
"""

v = [1, 2, 3]
w = [4, 5, 6]

# Producto punto
producto_punto = sum(v[i] * w[i] for i in range(len(v)))
print("v =", v)
print("w =", w)
print("v · w =", producto_punto)
