"""W3Resource 51: Convert Column DataType."""
import pandas as pd
import numpy as np

exam_data = {
    "attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    "name": [
        "Anastasia",
        "Dima",
        "Katherine",
        "James",
        "Emily",
        "Michael",
        "Matthew",
        "Laura",
        "Kevin",
        "Jonas",
    ],
    "qualify": ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes"],
    "score": [12.50, 9.10, 16.50, np.nan, 9.00, 20.00, 14.50, np.nan, 8.80, 19.13],
}
df = pd.DataFrame(exam_data)
df["score"] = df["score"].fillna(0)
print("Data types of the columns of the said DataFrame:")
print(df.dtypes)
print("\nNow change the Data type of 'score' column from float to int:")
df["score"] = df["score"].astype(int)
print(df)
print("\nData types of the columns of the DataFrame now:")
print(df.dtypes)
