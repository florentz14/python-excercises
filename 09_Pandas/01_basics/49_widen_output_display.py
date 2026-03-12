# -------------------------------------------------
# File Name: 49_widen_output_display.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Widens the output display of a DataFrame.
# -------------------------------------------------

# Import pandas library
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})

# Print the original DataFrame
print("Original DataFrame")
print(df)

# Set the display options
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

# Print the widened display
print("\nWidened display:")
print(df)
