# -------------------------------------------------
# File Name: 18_sum_attempts.py
# Author: Florentino Báez
# -------------------------------------------------
# Date: 3/11/2026
# Description: Summing examination attempts.
# -------------------------------------------------

# import libraries
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df_sum_attempts = pd.read_csv(csv_path)

# print the sum of the examination attempts by the students
print("Sum of the examination attempts by the students:")
print(df_sum_attempts["attempts"].sum())
