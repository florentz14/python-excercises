# -------------------------------------------------
# File Name: 14_pandas_seaborn.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Pandas + Matplotlib + Seaborn Integration.
#              Combine DataFrame data (Pandas), statistical
#              plots (Seaborn), and figure layout (Matplotlib).
#              Line, bar, box, and histogram with KDE.
# -------------------------------------------------

"""
Matplotlib - Example 8: Pandas + Matplotlib + Seaborn
========================================================
Combines: data in DataFrame (Pandas), plots with Seaborn, figure with Matplotlib.
Seaborn builds on Matplotlib and accepts DataFrames directly.
"""

import numpy as np
# numpy for random number generation
import pandas as pd
# pandas for DataFrame creation and data management
import matplotlib.pyplot as plt
# matplotlib for figure/axes layout
import seaborn as sns
# seaborn builds on matplotlib with statistical plot types

# --- Pandas: create data in DataFrame ---
# Create a sales DataFrame with monthly figures
ventas = pd.DataFrame({
    "mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
    "ventas": [120, 135, 150, 145, 160, 172],
    "gastos": [80, 85, 90, 88, 95, 100],
})

# Data by category (for boxplot and histogram)
# Seeded random generator for reproducible category data
rng = np.random.default_rng(42)
datos_cat = pd.DataFrame({
    "categoria": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
    # Generate normally distributed values: mean/std differ per category
    "valor": list(rng.normal(50, 10, 20)) + list(rng.normal(70, 12, 20)) + list(rng.normal(55, 8, 20)),
})

# Seaborn style (affects all subsequent plt calls)
# Apply Seaborn's whitegrid theme globally; husl palette has vivid colors
sns.set_theme(style="whitegrid", palette="husl")

# --- Matplotlib: figure with 2 rows, 2 columns ---
# 2x2 grid of subplots — each will host a different chart type
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 1) Line: sales and expenses (Seaborn with DataFrame)
# Access subplot by row, column index (top-left)
ax1 = axes[0, 0]
# Seaborn can read DataFrame columns directly via column names
sns.lineplot(data=ventas, x="mes", y="ventas", marker="o", ax=ax1, label="Ventas")
sns.lineplot(data=ventas, x="mes", y="gastos", marker="s", ax=ax1, label="Gastos")
ax1.set_title("Ventas vs gastos (Seaborn + Pandas)")
ax1.set_ylabel("Monto")

# 2) Bars: sales by month (Seaborn)
ax2 = axes[0, 1]
# ax= directs seaborn to draw on a specific subplot axis
sns.barplot(data=ventas, x="mes", y="ventas", ax=ax2)
ax2.set_title("Ventas por mes (Seaborn)")
ax2.set_ylabel("Ventas")

# 3) Boxplot by category (Seaborn with DataFrame)
ax3 = axes[1, 0]
# Boxplot groups data by 'categoria' and shows distribution of 'valor'
sns.boxplot(data=datos_cat, x="categoria", y="valor", ax=ax3)
ax3.set_title("Distribución por categoría (Seaborn)")
ax3.set_ylabel("Valor")

# 4) Histogram from DataFrame column (Seaborn)
ax4 = axes[1, 1]
# kde=True overlays a smooth Kernel Density Estimate curve
sns.histplot(data=datos_cat, x="valor", kde=True, ax=ax4)
ax4.set_title("Histograma + KDE (Seaborn)")
ax4.set_ylabel("Frecuencia")

# Super title for the entire 2x2 figure
fig.suptitle("Pandas + Matplotlib + Seaborn", fontsize=14)
plt.tight_layout()
plt.show()
