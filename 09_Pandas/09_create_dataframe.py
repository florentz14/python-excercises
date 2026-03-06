# ------------------------------------------------------------
# File: 09_create_dataframe.py
# Purpose: Create a DataFrame from a dictionary.
# Description: Keys become column names, list values become rows.
#              Shows columns, shape (rows, cols), basic display.
# ------------------------------------------------------------

import pandas as pd

# Dictionary: key = column name, value = list of row values
data = {
    "name": ["Anna", "Louis", "Mary"],
    "age": [25, 30, 28],
    "city": ["Madrid", "Barcelona", "Valencia"],
}

# Create DataFrame from dictionary
df = pd.DataFrame(data)
print(df)

print("\nColumns:", df.columns.tolist())
print("Dimensions:", df.shape)
