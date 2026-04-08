from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df = pd.read_csv(csv_path)
df.index = list("abcdefghij")

print("Selected columns:")
print(df[["name", "score"]])
