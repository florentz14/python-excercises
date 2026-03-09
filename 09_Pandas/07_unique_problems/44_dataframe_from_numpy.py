# -------------------------------------------------
# File Name: 44_dataframe_from_numpy.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 44 dataframe from numpy.
# -------------------------------------------------

"""Practice 44: DataFrame from NumPy Array."""
import pandas as pd
import numpy as np

arr = np.zeros((15, 3))
column_names = ["Column1", "Column2", "Column3"]
index_labels = [f"Index{i}" for i in range(1, 16)]
df_practice_44 = pd.DataFrame(arr, index=index_labels, columns=column_names)
print(df_practice_44)
