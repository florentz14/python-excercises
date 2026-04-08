from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df = pd.read_csv(csv_path)
df.index = list("abcdefghij")

print(f"Number of Rows: {df.shape[0]}")
print(f"Number of Columns: {df.shape[1]}")
