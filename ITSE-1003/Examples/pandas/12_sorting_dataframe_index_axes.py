# -------------------------------------------------
# File Name: 12_sorting_dataframe_index_axes.py
# Created: 2026-04-18
# Author: Florentino Báez
# Description: Sort a DataFrame by index or axes.
# -------------------------------------------------

import numpy as np
import pandas as pd


frame = pd.DataFrame(
    np.arange(16).reshape((4, 4)),
    index=["red", "blue", "yellow", "white"],
    columns=["ball", "pen", "pencil", "paper"],
)

print("Original DataFrame:")
print(frame)
print()

print("frame.sort_index()  # sort rows by index labels")
print(frame.sort_index())
print()

print("frame.sort_index(axis=1)  # sort columns by labels")
print(frame.sort_index(axis=1))
