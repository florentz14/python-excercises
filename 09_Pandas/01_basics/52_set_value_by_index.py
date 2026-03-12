# -------------------------------------------------
# File Name: 52_set_value_by_index.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Sets a value for a particular cell in a DataFrame by index.
# -------------------------------------------------

# Import pandas and numpy libraries
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR.parent / "data" / "exam_data.json"

# Load exam data from JSON
exam_data = pd.read_json(JSON_PATH).to_dict(orient="list")

# Create labels dynamically based on data length
labels = [chr(ord("a") + i) for i in range(len(exam_data["name"]))]

# Create a DataFrame with the exam data and the labels
df = pd.DataFrame(exam_data, index=labels)

# Set the value for the cell at index "i" and column "score"
df.loc["i", "score"] = 10.2

# Print the DataFrame
print("Set a given value for particular cell in the DataFrame")
print(df)
