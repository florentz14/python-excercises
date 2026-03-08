"""W3Resource 6: Selecting Specific Columns and Rows."""
import pandas as pd
import numpy as np

exam_data = {
    "name": [
        "Anastasia",
        "Dima",
        "Katherine",
        "James",
        "Emily",
        "Michael",
        "Matthew",
        "Laura",
        "Kevin",
        "Jonas",
    ],
    "score": [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    "attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    "qualify": ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes"],
}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
df = pd.DataFrame(exam_data, index=labels)

# Select 'score' and 'qualify' columns in rows 1, 3, 5, 6 (labels b, d, f, g)
print("Select specific columns and rows:")
print(df.loc[["b", "d", "f", "g"], ["score", "qualify"]])
