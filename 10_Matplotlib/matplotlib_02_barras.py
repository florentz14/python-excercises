"""
Matplotlib - Ejemplo 2: Gráfica de barras
==========================================
Tema: Matplotlib (10_Matplotlib)
Descripción: plt.bar(categorías, valores) para barras verticales.
"""

import matplotlib.pyplot as plt

categorias = ["A", "B", "C", "D"]
valores = [23, 45, 56, 33]

plt.figure(figsize=(5, 3))
plt.bar(categorias, valores, color="steelblue", edgecolor="black")
plt.xlabel("Categoría")
plt.ylabel("Valor")
plt.title("Gráfica de barras")
plt.tight_layout()
plt.show()
