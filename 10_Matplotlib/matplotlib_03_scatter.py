"""
Matplotlib - Ejemplo 3: Gráfica de dispersión (scatter)
=======================================================
Tema: Matplotlib (10_Matplotlib)
Descripción: plt.scatter(x, y) para puntos.
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 4, 3, 5, 6, 5, 8]

plt.figure(figsize=(5, 3))
plt.scatter(x, y, c="coral", s=80, alpha=0.8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráfica de dispersión")
plt.grid(True)
plt.tight_layout()
plt.show()
