# -------------------------------------------------
# File Name: 55_divide_dataframe_ratio.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Divides a DataFrame into two parts by a given ratio.
# -------------------------------------------------

# Import pandas and numpy libraries
import pandas as pd
import numpy as np

# Set the random seed to 42 to ensure reproducibility
np.random.seed(42)

# Create a random DataFrame with 10 rows and 2 columns
# The random numbers are normally distributed with mean 0 and standard deviation 1
df = pd.DataFrame(np.random.randn(10, 2))

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Get the length of the DataFrame
n = len(df)

# Calculate the size of the training set
train_size = int(0.7 * n)

# Sample the DataFrame to get the training set
train_df = df.sample(n=train_size, random_state=42)

# Drop the training set from the original DataFrame to get the test set (the remaining 30%)
test_df = df.drop(train_df.index)

# Print the training set
print("\n70% of the DataFrame:")
print(train_df)

# Print the remaining 30% of the DataFrame
print("\n30% of the DataFrame:")
print(test_df)
