# Archivo: datos_sistema.py
# Descripción: Datos compartidos para los ejemplos de sistemas de ecuaciones lineales

import numpy as np

# Sistema principal (código original)
A = np.array([[7, -5, 0], [5, -17, 5], [0, 5, -7]])
b = np.array([9, 0, 5])

# Múltiples sistemas (cada columna de B es un vector b)
B_multiple = np.array([[9, 12], [0, 0], [5, 6]]).T

# Sistema original (mismo que A, b)
A_original = np.array([[7, -5, 0], [5, -17, 5], [0, 5, -7]])
b_original = np.array([9, 0, 5])

# Sistema comentado (matriz B y vector d)
B_comentado = np.array([[10, -5, -5], [5, -12, 3], [5, 3, -8]])
d_comentado = np.array([12, 0, 6])
