"""
Vectores - Ejemplo 5: Magnitud (norma) de un vector
==================================================
Tema: Vectores (08_Matrices)
Descripción: ||v|| = sqrt(v[0]² + v[1]² + ...).
"""

import math

v = [3, 4]  # En R², ||v|| = 5

# Magnitud: raíz cuadrada de la suma de cuadrados
magnitud = math.sqrt(sum(x * x for x in v))
print("v =", v)
print("||v|| =", magnitud)

# Ejemplo en R³
u = [1, 0, 0]  # vector unitario
print("\nu =", u)
print("||u|| =", math.sqrt(sum(x * x for x in u)))
