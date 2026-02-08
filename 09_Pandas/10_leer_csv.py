# -------------------------------------------------
# File Name: 10_leer_csv.py
# Author: Florentino Báez
# Date: Pandas
# Description: Read a CSV File into a DataFrame.
#              pd.read_csv() loads a CSV file and returns
#              a DataFrame. Shows column names, shape,
#              and the first 5 rows with head().
# -------------------------------------------------

import pandas as pd
from pathlib import Path

# Path to data.csv in the project root (one folder above 09_Pandas)
ruta_csv = Path(__file__).parent.parent / "data.csv"

# Load CSV into a DataFrame
df = pd.read_csv(ruta_csv, encoding="utf-8")
print(df)

print("\nColumnas:", df.columns.tolist())   # Column names
print("Dimensiones:", df.shape)             # (rows, columns)

print("\nPrimeras 5 filas:")
print(df.head())                            # Display first 5 rows
