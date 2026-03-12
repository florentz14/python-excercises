# -------------------------------------------------
# File Name: 04_read_csv.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Read a CSV file into a DataFrame and show basic export options.
# -------------------------------------------------

# import libraries
import pandas as pd
from pathlib import Path

# path to CSV (data is in 09_Pandas/data/)
csv_path = Path(__file__).parent.parent / "data" / "data.csv"

# read CSV
df = pd.read_csv(csv_path, encoding="utf-8")

# print the DataFrame
print("Loaded DataFrame:")

# print the first 5 rows of the DataFrame
print(df.head())

# print the columns of the DataFrame
print("\nColumns:", df.columns.tolist())

# print the shape of the DataFrame
print("Shape:", df.shape)

# export the DataFrame to a CSV file
df.to_csv(Path(__file__).parent / "output.csv", index=False)

# print the exported file
print("\nExported DataFrame to output.csv")

# print the exported file
print(Path(__file__).parent / "output.csv")

