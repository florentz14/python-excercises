"""
Matplotlib - Ejemplo 1: Gráfica de línea
=========================================
Tema: Matplotlib (10_Matplotlib)
Descripción: plt.plot(x, y) para dibujar una curva.
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 5, 7]

plt.figure(figsize=(5, 3))
plt.plot(x, y, marker="o")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráfica de línea")
plt.grid(True)
plt.tight_layout()
plt.show()
