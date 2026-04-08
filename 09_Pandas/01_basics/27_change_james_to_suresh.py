# -------------------------------------------------
# File Name: 27_change_james_to_suresh.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Changing a Specific Name Value.
# -------------------------------------------------

# import libraries
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df_change_james_to_suresh = pd.read_csv(csv_path)
df_change_james_to_suresh.index = list("abcdefghij")

# change the name 'Sergio' to 'Suresh'
df_change_james_to_suresh["name"] = df_change_james_to_suresh["name"].replace("Sergio", "Suresh")
# print the DataFrame with the changed name
print("Change the name 'Sergio' to 'Suresh':")
print(df_change_james_to_suresh)
