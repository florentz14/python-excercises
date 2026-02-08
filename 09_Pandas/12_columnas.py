# -------------------------------------------------
# File Name: 12_columnas.py
# Author: Florentino Báez
# Date: Pandas
# Description: Select and Create Columns.
#              df["col"] returns a single column (Series).
#              df[["col1","col2"]] returns multiple columns
#              (DataFrame). Assign to df["new"] to create
#              a new computed column.
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "María"],
    "edad": [25, 30, 28],
    "saldo": [100, 200, 150],
})

# Select a single column (returns a Series)
print("Columna 'edad':\n", df["edad"])

# Select multiple columns (returns a DataFrame)
print("\nColumnas nombre y edad:\n", df[["nombre", "edad"]])

# Create a new column from an existing one
df["doble_saldo"] = df["saldo"] * 2
print("\nDataFrame con nueva columna:\n", df)
