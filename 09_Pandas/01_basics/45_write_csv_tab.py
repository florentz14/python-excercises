# -------------------------------------------------
# File Name: 45_write_csv_tab.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Writes a DataFrame to a CSV file with tab separator.
# -------------------------------------------------

# Import pandas and pathlib libraries
import pandas as pd
from pathlib import Path

# Create a DataFrame
df = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})

# Print the original DataFrame
print("Original DataFrame")
print(df)

# Write the DataFrame to a CSV file with tab separator
out = Path(__file__).parent / "new_file.csv"

# Write the DataFrame to a CSV file with tab separator
df.to_csv(out, sep="\t", index=False)

# Read the CSV file with tab separator
# Print the data from the new file
df2 = pd.read_csv(out, sep="\t")
print("\nData from new_file.csv file:")
print(df2)
