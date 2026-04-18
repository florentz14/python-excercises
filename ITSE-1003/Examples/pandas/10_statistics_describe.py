# -------------------------------------------------
# File Name: 10_statistics_describe.py
# Created: 2026-04-18
# Author: Florentino Báez
# Description: Summary statistics with describe().
# -------------------------------------------------

import numpy as np
import pandas as pd


frame = pd.DataFrame(
    np.arange(16).reshape((4, 4)),
    index=["red", "blue", "yellow", "white"],
    columns=["ball", "pen", "pencil", "paper"],
)

print("frame.describe():")
print(frame.describe())
