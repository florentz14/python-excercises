# -------------------------------------------------
# File Name: 18_filtering_sorting_fictional_army.py
# Author: Florentino Báez
# Date: Pandas
# Description: Filter and Sort a Fictional Army Dataset. Practice complex
#              filtering, multi-column sorting, and conditional selection
#              on military unit data.
# -------------------------------------------------

import pandas as pd

# Create sample fictional army data (no external CSV)
army_data = {
    "regiment": [
        "Nighthawks",
        "Nighthawks",
        "Dragoons",
        "Dragoons",
        "Scouts",
        "Scouts",
        "Nighthawks",
        "Dragoons",
        "Scouts",
        "Nighthawks",
        "Dragoons",
        "Scouts",
        "Nighthawks",
        "Dragoons",
        "Scouts",
    ],
    "company": ["1st", "1st", "2nd", "1st", "2nd", "1st", "2nd", "2nd", "1st", "2nd", "1st", "2nd", "1st", "1st", "2nd"],
    "name": [
        "Miller",
        "Johnson",
        "Williams",
        "Brown",
        "Jones",
        "Garcia",
        "Davis",
        "Rodriguez",
        "Martinez",
        "Wilson",
        "Anderson",
        "Taylor",
        "Thomas",
        "Moore",
        "Jackson",
    ],
    "preTestScore": [4, 24, 31, 2, 3, 55, 62, 70, 58, 45, 52, 48, 38, 65, 72],
    "postTestScore": [25, 94, 57, 62, 70, 80, 85, 90, 88, 75, 78, 82, 68, 92, 95],
}

df = pd.DataFrame(army_data)

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
