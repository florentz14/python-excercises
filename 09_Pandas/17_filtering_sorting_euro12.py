# -------------------------------------------------
# File Name: 17_filtering_sorting_euro12.py
# Author: Florentino Báez
# Date: Pandas
# Description: Filter and Sort Euro 2012 Football Data. Practice selecting
#              columns, filtering by goals, sorting teams, and selecting
#              specific rows.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parent / "euro12.csv"
df = pd.read_csv(csv_path)

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
