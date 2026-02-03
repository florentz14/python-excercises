"""
Matplotlib - Ejemplo 6: Gráfico de pastel (gráfico estadístico)
=================================================================
Tema: Matplotlib (10_Matplotlib)
Descripción: plt.pie() para mostrar proporciones o porcentajes de un total.
Útil para composición (gastos, votos, categorías).
"""

import matplotlib.pyplot as plt

etiquetas = ["Alimentación", "Transporte", "Ocio", "Otros"]
valores = [35, 25, 20, 20]
colores = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]

plt.figure(figsize=(5, 4))
plt.pie(valores, labels=etiquetas, autopct="%1.1f%%", colors=colores, startangle=90)
plt.title("Distribución de gastos (%)")
plt.axis("equal")
plt.tight_layout()
plt.show()
