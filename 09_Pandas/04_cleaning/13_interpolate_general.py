# -------------------------------------------------
# File Name: 108_interpolate_general.py
# Description: Fill missing values with interpolation
# -------------------------------------------------

import pandas as pd
import numpy as np

s = pd.Series([1, np.nan, np.nan, 4, 5])
print("Interpolated:")
print(s.interpolate())
