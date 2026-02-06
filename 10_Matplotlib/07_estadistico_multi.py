"""
Matplotlib - Ejemplo 7: Varios gráficos estadísticos en una figura
====================================================================
Tema: Matplotlib (10_Matplotlib)
Descripción: subplots con histograma y boxplot de los mismos datos.
"""

import matplotlib.pyplot as plt

datos = [12, 15, 18, 22, 25, 28, 30, 32, 35, 38, 40, 22, 24, 26, 29]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Histograma
ax1.hist(datos, bins=6, color="coral", edgecolor="white")
ax1.set_xlabel("Valor")
ax1.set_ylabel("Frecuencia")
ax1.set_title("Histograma")
ax1.grid(True, alpha=0.3)

# Boxplot
ax2.boxplot(datos, patch_artist=True)
ax2.set_ylabel("Valor")
ax2.set_title("Diagrama de caja")
ax2.grid(True, alpha=0.3, axis="y")

plt.suptitle("Análisis estadístico de una variable")
plt.tight_layout()
plt.show()
