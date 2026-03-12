# -------------------------------------------------
# File Name: 45_write_csv_tab.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 27 write csv tab.
# -------------------------------------------------

"""Practice 27: Write DataFrame to CSV (Tab Separator)."""
import pandas as pd
from pathlib import Path

df_practice_27 = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})
print("Original DataFrame")
print(df_practice_27)
out = Path(__file__).parent / "new_file.csv"
df_practice_27.to_csv(out, sep="\t", index=False)
df2 = pd.read_csv(out, sep="\t")
print("\nData from new_file.csv file:")
print(df2)
