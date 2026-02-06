"""
Matplotlib - Ejemplo 8: Pandas + Matplotlib + Seaborn
========================================================
Combina: datos en DataFrame (Pandas), gráficos con Seaborn, figura con Matplotlib.
Seaborn se apoya en Matplotlib y acepta DataFrames directamente.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Pandas: crear datos en DataFrame ---
ventas = pd.DataFrame({
    "mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
    "ventas": [120, 135, 150, 145, 160, 172],
    "gastos": [80, 85, 90, 88, 95, 100],
})

# Datos por categoría (para boxplot e histograma)
rng = np.random.default_rng(42)
datos_cat = pd.DataFrame({
    "categoria": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
    "valor": list(rng.normal(50, 10, 20)) + list(rng.normal(70, 12, 20)) + list(rng.normal(55, 8, 20)),
})

# Estilo Seaborn (afecta a todos los plt siguientes)
sns.set_theme(style="whitegrid", palette="husl")

# --- Matplotlib: figura con 2 filas, 2 columnas ---
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 1) Línea: ventas y gastos (Seaborn con DataFrame)
ax1 = axes[0, 0]
sns.lineplot(data=ventas, x="mes", y="ventas", marker="o", ax=ax1, label="Ventas")
sns.lineplot(data=ventas, x="mes", y="gastos", marker="s", ax=ax1, label="Gastos")
ax1.set_title("Ventas vs gastos (Seaborn + Pandas)")
ax1.set_ylabel("Monto")

# 2) Barras: ventas por mes (Seaborn)
ax2 = axes[0, 1]
sns.barplot(data=ventas, x="mes", y="ventas", ax=ax2)
ax2.set_title("Ventas por mes (Seaborn)")
ax2.set_ylabel("Ventas")

# 3) Boxplot por categoría (Seaborn con DataFrame)
ax3 = axes[1, 0]
sns.boxplot(data=datos_cat, x="categoria", y="valor", ax=ax3)
ax3.set_title("Distribución por categoría (Seaborn)")
ax3.set_ylabel("Valor")

# 4) Histograma desde columna del DataFrame (Seaborn)
ax4 = axes[1, 1]
sns.histplot(data=datos_cat, x="valor", kde=True, ax=ax4)
ax4.set_title("Histograma + KDE (Seaborn)")
ax4.set_ylabel("Frecuencia")

fig.suptitle("Pandas + Matplotlib + Seaborn", fontsize=14)
plt.tight_layout()
plt.show()
