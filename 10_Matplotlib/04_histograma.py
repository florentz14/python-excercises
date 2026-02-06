"""
Matplotlib - Ejemplo 4: Histograma (gráfico estadístico)
=========================================================
Tema: Matplotlib (10_Matplotlib)
Descripción: plt.hist() para ver la distribución de frecuencias de datos.
Útil para ver cómo se distribuyen los valores (normal, sesgada, etc.).
"""

import matplotlib.pyplot as plt

# Datos: por ejemplo, notas de un examen
notas = [4.5, 5.0, 6.2, 5.8, 7.1, 6.5, 5.2, 8.0, 7.5, 6.0, 5.5, 6.8, 4.0, 7.2, 6.1]

plt.figure(figsize=(6, 4))
plt.hist(notas, bins=6, color="steelblue", edgecolor="white")
plt.xlabel("Nota")
plt.ylabel("Frecuencia")
plt.title("Histograma: distribución de notas")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
