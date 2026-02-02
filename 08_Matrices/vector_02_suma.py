"""
Vectores - Ejemplo 2: Suma de vectores
=======================================
Tema: Vectores (08_Matrices)
Descripción: Sumar dos vectores componente a componente.
"""

v = [1, 2, 3]
w = [4, 5, 6]

# Suma: v + w = (v[0]+w[0], v[1]+w[1], v[2]+w[2])
suma = [v[i] + w[i] for i in range(len(v))]
print("v =", v)
print("w =", w)
print("v + w =", suma)
