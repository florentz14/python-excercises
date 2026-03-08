"""W3Resource 67: Split DataFrame into Two Random Subsets."""
import pandas as pd

df = pd.DataFrame(
    {
        "name": ["Alberto Franco", "Gino Mcneill", "Ryan Parkes", "Eesha Hinton", "Syed Wharton"],
        "date_of_birth": ["17/05/2002", "16/02/1999", "25/09/1998", "11/05/2002", "15/09/1997"],
        "age": [18, 21, 22, 22, 23],
    }
)
print("Original Dataframe and shape:")
print(df)
print(df.shape)
n = len(df)
subset1 = df.sample(n=int(n * 0.6), random_state=42)
subset2 = df.drop(subset1.index)
print("\nSubset-1 and shape:")
print(subset1)
print(subset1.shape)
print("\nSubset-2 and shape:")
print(subset2)
print(subset2.shape)
