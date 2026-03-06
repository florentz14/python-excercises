# Archivo: datos_ejemplo_33.py
# Descripción: Datos del sistema de ecuaciones específico (ejemplo 33)
# Sistema: x + y + z = 2,  2x + z = 1,  x + 2y = 5

import numpy as np

# Matriz de coeficientes
A = np.array([[1, 1, 1], [2, 0, 1], [1, 2, 0]])
# Vector de términos independientes
b = np.array([2, 1, 5])
