# ------------------------------------------------------------
# Basic case: Read and write CSV
# ------------------------------------------------------------

import pandas as pd
from pathlib import Path

# Path to CSV (data is in 09_Pandas/data/)
data_path = Path(__file__).parent.parent / "data"
csv_path = data_path / "data.csv"

# Read CSV
df = pd.read_csv(csv_path, encoding="utf-8")
print("Loaded DataFrame:")
print(df.head())
print("\nColumns:", df.columns.tolist())
print("Shape:", df.shape)

# Export to CSV (example: save in basics/)
# df.to_csv(Path(__file__).parent / "output.csv", index=False)
