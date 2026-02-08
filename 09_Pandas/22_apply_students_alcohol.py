# -------------------------------------------------
# File Name: 22_apply_students_alcohol.py
# Author: Florentino Báez
# Date: Pandas
# Description: Apply Functions to Student Alcohol Consumption Data. Use apply(),
#              map(), and lambda to transform grades, categorize consumption
#              levels, and create derived columns.
# -------------------------------------------------

import pandas as pd

# Create sample student alcohol consumption data (inline, no external CSV)
data = {
    "school": ["GP", "GP", "MS", "MS", "GP", "MS", "GP", "GP", "MS", "GP", "MS", "GP", "GP", "MS", "GP"],
    "sex": ["F", "F", "M", "M", "F", "M", "F", "M", "M", "F", "F", "M", "F", "M", "M"],
    "age": [18, 17, 15, 15, 16, 16, 18, 17, 15, 16, 17, 18, 16, 15, 17],
    "studytime": [2, 2, 2, 3, 2, 1, 1, 2, 3, 2, 1, 4, 2, 2, 3],
    "failures": [0, 0, 3, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 0],
    "Dalc": [1, 1, 3, 1, 2, 4, 1, 2, 5, 1, 3, 2, 2, 4, 2],
    "Walc": [1, 1, 4, 1, 2, 5, 1, 3, 5, 2, 4, 3, 3, 5, 3],
    "G1": [5, 5, 8, 14, 10, 10, 10, 11, 6, 12, 10, 12, 10, 8, 14],
    "G2": [6, 5, 9, 14, 10, 11, 10, 11, 8, 12, 11, 12, 11, 9, 14],
    "G3": [6, 6, 10, 14, 10, 11, 10, 11, 9, 12, 11, 12, 11, 10, 14],
}
df = pd.DataFrame(data)

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
