# -------------------------------------------------
# File Name: 22_apply_students_alcohol.py
# Author: Florentino Báez
# Date: Pandas
# Description: Apply Functions to Student Alcohol Consumption Data. Use apply(),
#              map(), and lambda to transform grades, categorize consumption
#              levels, and create derived columns.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parent / "students_alcohol.csv"
df = pd.read_csv(csv_path)

print("=" * 60)
print("ORIGINAL DATAFRAME (school, sex, age, studytime, failures, Dalc, Walc, G1, G2, G3)")
print("=" * 60)
print(df)
print()

# Use apply() with lambda to categorize G3 into 'Pass'/'Fail' (>=10 pass)
df["G3_result"] = df["G3"].apply(lambda x: "Pass" if x >= 10 else "Fail")
print("G3 result (Pass/Fail, threshold 10):")
print(df[["G3", "G3_result"]])
print()

# Use apply() to create 'total_alcohol' = Dalc + Walc
df["total_alcohol"] = df.apply(lambda row: row["Dalc"] + row["Walc"], axis=1)
print("Total alcohol (Dalc + Walc):")
print(df[["Dalc", "Walc", "total_alcohol"]])
print()

# Use map() to convert sex column: 'F' -> 'Female', 'M' -> 'Male'
df["sex_label"] = df["sex"].map({"F": "Female", "M": "Male"})
print("Sex mapped to Female/Male:")
print(df[["sex", "sex_label"]])
print()

# Apply a custom function to calculate grade average (G1+G2+G3)/3
def grade_average(row):
    return (row["G1"] + row["G2"] + row["G3"]) / 3

df["grade_avg"] = df.apply(grade_average, axis=1)
print("Grade average (G1+G2+G3)/3:")
print(df[["G1", "G2", "G3", "grade_avg"]])
print()

# Use map on Series to highlight high alcohol consumption
df["high_alc_flag"] = df["total_alcohol"].map(lambda x: "High" if x >= 6 else "Normal")
print("High alcohol flag (total_alcohol >= 6):")
print(df[["total_alcohol", "high_alc_flag"]])
print()

# Categorize studytime: 1='Low', 2='Medium', 3='High', 4='Very High'
studytime_map = {1: "Low", 2: "Medium", 3: "High", 4: "Very High"}
df["studytime_category"] = df["studytime"].map(studytime_map)
print("Studytime category:")
print(df[["studytime", "studytime_category"]])
print()

# Create a binary column: 'high_risk' = True if total_alcohol > 6 AND failures > 0
df["high_risk"] = df.apply(lambda row: row["total_alcohol"] > 6 and row["failures"] > 0, axis=1)
print("High risk (total_alcohol > 6 AND failures > 0):")
print(df[["total_alcohol", "failures", "high_risk"]])
print()

print("Final dataframe with derived columns (sample):")
print(df.head(10))
