# -------------------------------------------------
# File Name: 03_df_index_labels.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Create a DataFrame with specified index labels.
# -------------------------------------------------

# import libraries
import pandas as pd
from df_index_labels_data import data, labels

# Create a DataFrame from the dictionary with the index labels
df = pd.DataFrame(data, index=labels)

# print the DataFrame
print(df)
