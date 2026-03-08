"""W3Resource 70: Convert Continuous Column to Categorical."""
import pandas as pd

df = pd.DataFrame(
    {
        "Name": ["Alberto Franco", "Gino Mcneill", "Ryan Parkes", "Eesha Hinton", "Syed Wharton", "Extra"],
        "Age": [18, 22, 40, 50, 80, 5],
    }
)
bins = [0, 18, 60, 100]
labels = ["kids", "adult", "elderly"]
df["age_groups"] = pd.cut(df["Age"], bins=bins, labels=labels)
print("Age group:")
print(df["age_groups"])
