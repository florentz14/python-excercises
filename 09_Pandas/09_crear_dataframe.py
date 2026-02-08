# -------------------------------------------------
# File Name: 09_crear_dataframe.py
# Author: Florentino Báez
# Date: Pandas
# Description: Create a DataFrame from a Dictionary.
#              A DataFrame is a 2D table (like Excel).
#              Dictionary keys become column names, and
#              list values become row data. Shows columns,
#              shape (rows, cols), and basic display.
# -------------------------------------------------

import pandas as pd

# Dictionary: key = column name, value = list of row values
datos = {
    "nombre": ["Ana", "Luis", "María"],
    "edad": [25, 30, 28],
    "ciudad": ["Madrid", "Barcelona", "Valencia"],
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(datos)
print(df)

print("\nColumnas:", df.columns.tolist())   # List of column names
print("Dimensiones:", df.shape)             # (rows, columns)
