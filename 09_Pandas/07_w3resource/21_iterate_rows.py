"""W3Resource 21: Iterating Over DataFrame Rows."""
import pandas as pd

exam_data = [
    {"name": "Anastasia", "score": 12.5},
    {"name": "Dima", "score": 9},
    {"name": "Katherine", "score": 16.5},
]
df = pd.DataFrame(exam_data)

for _, row in df.iterrows():
    print(row["name"], row["score"])
