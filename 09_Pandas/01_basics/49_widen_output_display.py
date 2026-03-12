# -------------------------------------------------
# File Name: 49_widen_output_display.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 30 widen output display.
# -------------------------------------------------

"""Practice 30: Widen Output Display."""
import pandas as pd

df_practice_30 = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})
print("Original DataFrame")
print(df_practice_30)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)
print("\nWidened display:")
print(df_practice_30)
