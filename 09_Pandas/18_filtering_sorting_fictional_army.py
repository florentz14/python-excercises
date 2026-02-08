# -------------------------------------------------
# File Name: 18_filtering_sorting_fictional_army.py
# Author: Florentino Báez
# Date: Pandas
# Description: Filter and Sort a Fictional Army Dataset. Practice complex
#              filtering, multi-column sorting, and conditional selection
#              on military unit data.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parent / "fictional_army.csv"
df = pd.read_csv(csv_path)

# Filter soldiers with preTestScore > 50
print("=== FILTER: preTestScore > 50 ===")
high_pre = df[df["preTestScore"] > 50]
print(high_pre)
print()

# Filter Nighthawks regiment only
print("=== FILTER: Nighthawks regiment only ===")
nighthawks = df[df["regiment"] == "Nighthawks"]
print(nighthawks)
print()

# Sort by postTestScore descending
print("=== SORT BY postTestScore (descending) ===")
sorted_post = df.sort_values(by="postTestScore", ascending=False)
print(sorted_post)
print()

# Filter soldiers where postTestScore > preTestScore (improved)
print("=== FILTER: postTestScore > preTestScore (improved) ===")
improved = df[df["postTestScore"] > df["preTestScore"]]
print(improved)
print()

# Multiple conditions: regiment == 'Dragoons' AND postTestScore > 50
print("=== FILTER: Dragoons AND postTestScore > 50 ===")
dragoons_high = df[(df["regiment"] == "Dragoons") & (df["postTestScore"] > 50)]
print(dragoons_high)
print()

# Create new column 'improvement' = postTestScore - preTestScore
df["improvement"] = df["postTestScore"] - df["preTestScore"]
print("=== NEW COLUMN: improvement ===")
print(df[["name", "regiment", "preTestScore", "postTestScore", "improvement"]])
print()

# Sort by regiment then by postTestScore
print("=== SORT BY regiment, then postTestScore ===")
sorted_regiment_post = df.sort_values(by=["regiment", "postTestScore"], ascending=[True, False])
print(sorted_regiment_post)
print()

# Find top 5 soldiers by postTestScore
print("=== TOP 5 SOLDIERS BY postTestScore ===")
top5 = df.nlargest(5, "postTestScore")
print(top5)
