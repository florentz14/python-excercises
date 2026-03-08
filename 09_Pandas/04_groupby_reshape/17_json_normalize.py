# -------------------------------------------------
# File Name: 113_json_normalize.py
# Description: Flatten JSON into DataFrame
# -------------------------------------------------

import pandas as pd

data = [{"name": "Alice", "scores": {"math": 90, "english": 85}}, {"name": "Bob", "scores": {"math": 75, "english": 88}}]
df = pd.json_normalize(data)
print(df)
