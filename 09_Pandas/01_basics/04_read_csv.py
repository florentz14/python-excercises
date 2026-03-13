# -------------------------------------------------
# File Name: 04_read_csv.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Read a CSV file into a DataFrame and show basic export options.
# -------------------------------------------------

# import libraries
import pandas as pd
from pathlib import Path

# Define the path to the sales CSV file
# The CSV file is in the data folder of the parent directory
csv_path = Path(__file__).parent.parent / "data" / "data_sales.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_path, encoding="utf-8")

# Print the DataFrame
print("Loaded DataFrame:")

# Print the first 5 rows of the DataFrame
print(df.head())

# Print the columns of the DataFrame
print("\nColumns:", df.columns.tolist())

# Print the shape of the DataFrame
print("Shape:", df.shape)

# Export the DataFrame to a CSV file
# The CSV file is in the parent directory
df.to_csv(Path(__file__).parent / "output.csv", index=False)

# Print the exported file
print("\nExported DataFrame to output.csv")

# Print the exported file
print(Path(__file__).parent / "output.csv")

