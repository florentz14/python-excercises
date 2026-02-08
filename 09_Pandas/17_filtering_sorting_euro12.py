# -------------------------------------------------
# File Name: 17_filtering_sorting_euro12.py
# Author: Florentino Báez
# Date: Pandas
# Description: Filter and Sort Euro 2012 Football Data. Practice selecting
#              columns, filtering by goals, sorting teams, and selecting
#              specific rows.
# -------------------------------------------------

import pandas as pd

# Create Euro 2012-style DataFrame with European teams and realistic stats (no external CSV)
euro_data = {
    "Team": [
        "Germany",
        "Spain",
        "Italy",
        "England",
        "France",
        "Portugal",
        "Netherlands",
        "Greece",
        "Croatia",
        "Poland",
    ],
    "Goals": [10, 12, 6, 5, 3, 6, 2, 5, 4, 2],
    "Shots on target": [32, 43, 22, 18, 12, 20, 8, 14, 15, 9],
    "Shots off target": [18, 12, 25, 22, 15, 18, 12, 20, 16, 14],
    "Shooting Accuracy": [64.0, 78.0, 47.0, 45.0, 44.0, 53.0, 40.0, 41.0, 48.0, 39.0],
    "Goals-to-shots": [0.20, 0.22, 0.13, 0.13, 0.11, 0.16, 0.10, 0.15, 0.13, 0.09],
    "Passes": [5876, 6142, 4512, 3982, 3921, 4692, 3580, 3210, 3850, 2980],
    "Pass Accuracy": [90.0, 91.0, 88.0, 86.0, 85.0, 87.0, 82.0, 79.0, 84.0, 78.0],
}

df = pd.DataFrame(euro_data)

# Select only Team and Goals columns
print("=== SELECT: Team and Goals columns ===")
team_goals = df[["Team", "Goals"]]
print(team_goals)
print()

# Filter teams with more than 6 goals
print("=== FILTER: teams with Goals > 6 ===")
high_goals = df[df["Goals"] > 6]
print(high_goals)
print()

# Sort by Goals descending
print("=== SORT BY Goals (descending) ===")
sorted_goals = df.sort_values(by="Goals", ascending=False)
print(sorted_goals)
print()

# Filter teams that start with 'G'
print("=== FILTER: teams starting with 'G' ===")
starts_with_g = df[df["Team"].str.startswith("G")]
print(starts_with_g)
print()

# Select first 5 teams (first 5 rows)
print("=== FIRST 5 TEAMS ===")
first_five = df.head(5)
print(first_five)
print()

# Count teams with shooting accuracy > 50%
print("=== COUNT: Shooting Accuracy > 50% ===")
accurate_teams = df[df["Shooting Accuracy"] > 50]
count_accurate = len(accurate_teams)
print(f"Number of teams with shooting accuracy > 50%: {count_accurate}")
print(accurate_teams[["Team", "Shooting Accuracy"]])
print()

# Find the team with most goals
print("=== TEAM WITH MOST GOALS ===")
max_goals_team = df.loc[df["Goals"].idxmax(), "Team"]
max_goals_value = df["Goals"].max()
print(f"Team: {max_goals_team}, Goals: {max_goals_value}")
