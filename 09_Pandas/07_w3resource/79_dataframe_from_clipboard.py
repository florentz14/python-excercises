"""W3Resource 79: Create DataFrame from Clipboard."""
import pandas as pd

# Requires data in clipboard (e.g. from Excel). Falls back to sample if empty.
try:
    df = pd.read_clipboard()
    if df.empty:
        raise ValueError("Clipboard empty")
except Exception:
    df = pd.DataFrame({"1": [2, 4, 2], "2": [3, 5, 3], "3": [4, 1, 7], "4": [5, 0, 8]})
    print("(Using sample data - copy from Excel and run for real clipboard)")
print("Data from clipboard to DataFrame:")
print(df)
