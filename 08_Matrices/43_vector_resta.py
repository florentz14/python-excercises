"""
Vectores - Ejemplo 6: Resta de vectores
=======================================
Tema: Vectores (08_Matrices)
Descripción: Restar dos vectores componente a componente: v - w.
"""

v = [5, 7, 2]
w = [1, 3, 4]

resta = [v[i] - w[i] for i in range(len(v))]
print("v =", v)
print("w =", w)
print("v - w =", resta)
