"""
Matplotlib - Ejemplo 5: Diagrama de caja (boxplot, gráfico estadístico)
========================================================================
Tema: Matplotlib (10_Matplotlib)
Descripción: plt.boxplot() muestra mediana, cuartiles y valores atípicos.
Útil para comparar distribuciones y detectar outliers.
"""

import matplotlib.pyplot as plt

# Datos: ejemplos por grupo (A, B, C)
datos = [
    [22, 25, 28, 30, 32, 35, 38],
    [18, 24, 27, 29, 31, 36, 42],
    [20, 23, 26, 28, 30, 33, 45],
]

plt.figure(figsize=(6, 4))
cajas = plt.boxplot(datos, labels=["Grupo A", "Grupo B", "Grupo C"], patch_artist=True)
for caja in cajas["boxes"]:
    caja.set_facecolor("lightblue")
plt.ylabel("Valor")
plt.title("Diagrama de caja (boxplot)")
plt.grid(True, alpha=0.3, axis="y")
plt.tight_layout()
plt.show()
