# -------------------------------------------------
# File Name: 51_convert_column_datatype.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 51 convert column datatype.
# -------------------------------------------------

"""Practice 51: Convert Column DataType."""
import pandas as pd
import numpy as np

exam_data = {
    "attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    "name": [
        "Valeria",
        "Thiago",
        "Camila",
        "Sergio",
        "Daniela",
        "Bruno",
        "Renata",
        "Nicolas",
        "Aitana",
        "Gael",
    ],
    "qualify": ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes"],
    "score": [12.50, 9.10, 16.50, np.nan, 9.00, 20.00, 14.50, np.nan, 8.80, 19.13],
}
df_practice_51 = pd.DataFrame(exam_data)
df_practice_51["score"] = df_practice_51["score"].fillna(0)
print("Data types of the columns of the said DataFrame:")
print(df_practice_51.dtypes)
print("\nNow change the Data type of 'score' column from float to int:")
df_practice_51["score"] = df_practice_51["score"].astype(int)
print(df_practice_51)
print("\nData types of the columns of the DataFrame now:")
print(df_practice_51.dtypes)
