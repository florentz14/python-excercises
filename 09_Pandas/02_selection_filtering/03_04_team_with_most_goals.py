from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "euro12.csv"
df = pd.read_csv(csv_path)

max_goals_team = df.loc[df["Goals"].idxmax(), "Team"]
max_goals_value = df["Goals"].max()

print(f"Team with most goals: {max_goals_team}, Goals: {max_goals_value}")
