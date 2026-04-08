import pandas as pd


df = pd.DataFrame(
    {"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]}
)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

print("Widened display:")
print(df)
