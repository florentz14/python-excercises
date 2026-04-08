# -------------------------------------------------
# File Name: 52_sales_visualization_miniproject.py
# Author: Florentino Baez
# Date: 09_Pandas
# Description: Mini project with cleaning + sales visualizations.
# -------------------------------------------------

import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
EXPORT_DIR = BASE_DIR.parent / "data" / "exports"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

# --- PHASE 1: PREPARATION ---
# Create a DataFrame with the sales data
df_ventas = pd.DataFrame(
    {
        "order_id": [101, 102, 103, 104, 105, 106, 101],
        "product_id": ["ball", "pencil", "pen", "mug", "ashtray", "laptop", "ball"],
        "qty": [2, 5, 1, 3, 1, 10, 2],
        "email_cliente": [
            "juan@mail.com",
            "ana@gmail.com",
            "PEDRO@OUTLOOK.COM",
            "luis@mail.net",
            "marta@mail.com",
            "error_mail",
            "juan@mail.com",
        ],
    }
)

# Create a DataFrame with the prices data
df_precios = pd.DataFrame(
    {
        "product_id": ["ball", "pencil", "pen", "mug", "ashtray"],
        "price": [12.50, 1.20, 2.00, 15.00, 5.00],
    }
)

# Merge the sales and prices DataFrames on the product_id column
ventas_full = pd.merge(df_ventas, df_precios, on="product_id", how="left")

# Create a Series with the emergency prices
precios_emergencia = pd.Series(np.nan, index=ventas_full.index)
precios_emergencia.loc[ventas_full["product_id"] == "laptop"] = 500.00
ventas_full["price"] = ventas_full["price"].fillna(precios_emergencia)

# --- PHASE 2: CLEANING ---
# Drop the duplicate rows
ventas_full = ventas_full.drop_duplicates()
ventas_full["email_cliente"] = ventas_full["email_cliente"].str.lower().str.strip()

# Create a regex for the email
regex_email = re.compile(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}")
ventas_full["email_valido"] = ventas_full["email_cliente"].apply(
    lambda value: value if regex_email.fullmatch(value) else np.nan
)

# Create a dictionary with the category mapping
categoria_map = {
    "ball": "Deportes",
    "pencil": "Papeleria",
    "pen": "Papeleria",
    "mug": "Hogar",
    "ashtray": "Hogar",
    "laptop": "Tecnologia",
}
ventas_full["categoria"] = ventas_full["product_id"].apply(
    lambda value: categoria_map.get(str(value), "Otros")
)

# Create a new column with the sales volume
ventas_full["volumen_venta"] = pd.cut(
    ventas_full["qty"], bins=[0, 2, 5, 20], labels=["Bajo", "Medio", "Alto"]
)

# Create a new column with the subtotal
ventas_full["subtotal"] = ventas_full["qty"] * ventas_full["price"]

# Create a pivot table with the summary
resumen_categoria = pd.DataFrame(
    ventas_full.groupby("categoria", as_index=False).agg(subtotal=("subtotal", "sum"))
)
resumen_pivot = (
    ventas_full.pivot_table(
        index="categoria",
        columns="volumen_venta",
        values="subtotal",
        aggfunc="sum",
        observed=False,
    )
    .fillna(0)
    .round(2)
)

# --- PHASE 3: VISUALIZATION ---
# Create the path for the bar chart
bar_path = EXPORT_DIR / "sales_subtotal_by_category.png"
# Create the path for the heatmap
heatmap_path = EXPORT_DIR / "sales_pivot_heatmap.png"

# Create the bar chart
plt.figure(figsize=(8, 4.5))
x_labels = [str(value) for value in resumen_categoria["categoria"]]
y_values = [float(value) for value in resumen_categoria["subtotal"]]
plt.bar(x_labels, y_values, color="#4C78A8")
plt.title("Subtotal de Ventas por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Subtotal ($)")
plt.tight_layout()
plt.savefig(bar_path, dpi=120)
plt.close()

# Create the heatmap
plt.figure(figsize=(7, 4.5))
matrix = np.asarray(resumen_pivot.to_numpy(), dtype=float)
plt.imshow(matrix, cmap="Blues", aspect="auto")
plt.title("Matriz de Ventas: Categoria vs Volumen")
plt.xlabel("Volumen de Venta")
plt.ylabel("Categoria")
xtick_labels = [str(value) for value in resumen_pivot.columns]
ytick_labels = [str(value) for value in resumen_pivot.index]
plt.xticks(ticks=range(len(xtick_labels)), labels=xtick_labels)
plt.yticks(ticks=range(len(ytick_labels)), labels=ytick_labels)
plt.colorbar(label="Subtotal ($)")

# Add the text to the heatmap
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        plt.text(j, i, f"{matrix[i, j]:.0f}", ha="center", va="center", color="black")

# Save the heatmap
plt.tight_layout()
plt.savefig(heatmap_path, dpi=120)
plt.close()

# Print the summary of the sales data (mini-project)
print("=" * 66)
print("          MINI-PROYECTO DE VISUALIZACION DE VENTAS")
print("=" * 66)
print(f"Filas finales: {len(ventas_full)}")
print(f"Subtotal total: ${ventas_full['subtotal'].sum():.2f}")
print(f"Correos validos: {ventas_full['email_valido'].notna().sum()} / {len(ventas_full)}")
print("\nArchivos generados:")
print(f"- {bar_path}")
print(f"- {heatmap_path}")
