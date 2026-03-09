# -------------------------------------------------
# File Name: 79_dataframe_from_clipboard.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 79 dataframe from clipboard.
# -------------------------------------------------

"""Practice 79: Create DataFrame from Clipboard."""
import pandas as pd

# Requires data in clipboard (e.g. from Excel). Falls back to sample if empty.
try:
    df_practice_79 = pd.read_clipboard()
    if df_practice_79.empty:
        raise ValueError("Clipboard empty")
except Exception:
    data = {"1": [2, 4, 2], "2": [3, 5, 3], "3": [4, 1, 7], "4": [5, 0, 8]}
    df_practice_79 = pd.DataFrame(data)
    print("(Using sample data - copy from Excel and run for real clipboard)")
print("Data from clipboard to DataFrame:")
print(df_practice_79)
