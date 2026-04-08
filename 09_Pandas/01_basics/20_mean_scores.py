# -------------------------------------------------
# File Name: 20_mean_scores.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Calculating the mean of scores for each different student in the data frame.
# -------------------------------------------------

# import libraries
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df_mean_scores = pd.read_csv(csv_path)

# print the mean score for each different student in the data frame
print("Mean score for each different student in data frame:")
print(df_mean_scores["score"].mean())
