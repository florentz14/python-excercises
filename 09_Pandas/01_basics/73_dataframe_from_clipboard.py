# -------------------------------------------------
# File Name: 73_dataframe_from_clipboard.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Creates a DataFrame from clipboard or fallback sample data.
# -------------------------------------------------

# import libraries
import pandas as pd

# read clipboard data and fallback to sample if clipboard is empty
try:
    df = pd.read_clipboard()
    if df.empty:
        raise ValueError("Clipboard empty")
except Exception:
    data = {"1": [2, 4, 2], "2": [3, 5, 3], "3": [4, 1, 7], "4": [5, 0, 8]}
    df = pd.DataFrame(data)
    print("(Using sample data - copy from Excel and run for real clipboard)")

# print resulting DataFrame
print("Data from clipboard to DataFrame:")
print(df)
