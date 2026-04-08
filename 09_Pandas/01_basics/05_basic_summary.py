# -------------------------------------------------
# File Name: 05_basic_summary.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Create a DataFrame with basic summary information.
# -------------------------------------------------

# import libraries
import pandas as pd
from basic_summary_data import exam_data, labels

# Create a DataFrame from the dictionary with the index labels
df = pd.DataFrame(exam_data, index=labels)

# Print the DataFrame
print("Summary of the basic information about this DataFrame and its data:")
print(df.info())
