"""W3Resource 71: Display Memory Usage of DataFrame and Columns."""
import pandas as pd

df = pd.DataFrame(
    {
        "Name": ["Alberto Franco", "Gino Mcneill", "Ryan Parkes", "Eesha Hinton", "Syed Wharton"],
        "Date_Of_Birth": ["17/05/2002", "16/02/1999", "25/09/1998", "11/05/2002", "15/09/1997"],
        "Age": [18.5, 21.2, 22.5, 22.0, 23.0],
    }
)
print("Original DataFrame:")
print(df)
print("\nGlobal usage of memory of the DataFrame:")
print(df.info(memory_usage="deep"))
print("\nThe usage of memory of every column of the said DataFrame:")
print(df.memory_usage(deep=True))
