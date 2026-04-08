from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df = pd.read_csv(csv_path)
df.index = list("abcdefghij")

print("Rows where score between 15 and 20 (inclusive):")
print(df[(df["score"] >= 15) & (df["score"] <= 20)])
