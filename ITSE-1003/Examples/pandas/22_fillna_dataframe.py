# -------------------------------------------------
# File Name: 22_fillna_dataframe.py
# Created: 2026-04-18
# Author: Florentino Báez
# Description: Fill missing values with fillna on DataFrame.
# -------------------------------------------------

import numpy as np
import pandas as pd


frame3 = pd.DataFrame(
    [[6, np.nan, 6], [np.nan, np.nan, np.nan], [2, np.nan, 5]],
    index=["blue", "green", "red"],
    columns=["ball", "mug", "pen"],
)

print("Original DataFrame:")
print(frame3)
print()

print("frame3.fillna(0):")
print(frame3.fillna(0))
print()

print("frame3.fillna({'ball': 1, 'mug': 0, 'pen': 99}):")
print(frame3.fillna({"ball": 1, "mug": 0, "pen": 99}))
