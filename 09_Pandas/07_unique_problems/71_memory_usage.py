# -------------------------------------------------
# File Name: 71_memory_usage.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 71 memory usage.
# -------------------------------------------------

"""Practice 71: Display Memory Usage of DataFrame and Columns."""
import pandas as pd

data = {"Name": ["Alberto Franco", "Gino Mcneill", "Ryan Parkes", "Eesha Hinton", "Syed Wharton"], "Date_Of_Birth": ["17/05/2002", "16/02/1999", "25/09/1998", "11/05/2002", "15/09/1997"], "Age": [18.5, 21.2, 22.5, 22.0, 23.0]}
df_practice_71 = pd.DataFrame(data)
print("Original DataFrame:")
print(df_practice_71)
print("\nGlobal usage of memory of the DataFrame:")
print(df_practice_71.info(memory_usage="deep"))
print("\nThe usage of memory of every column of the said DataFrame:")
print(df_practice_71.memory_usage(deep=True))
