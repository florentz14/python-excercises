# -------------------------------------------------
# File Name: 115_corr_cov.py
# Description: Correlation and covariance
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [2, 4, 5, 4, 5]})
print("Correlation:")
print(df.corr())
print("\nCovariance:")
print(df.cov())
