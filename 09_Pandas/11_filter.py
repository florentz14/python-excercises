# ------------------------------------------------------------
# File: 11_filter.py
# Purpose: Filter DataFrame rows by condition.
# Description: Use df[condition] to select rows meeting a boolean condition.
#              Combine with & (AND) and | (OR). Wrap each condition in parens.
# ------------------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "name": ["Anna", "Louis", "Mary", "Peter"],
    "age": [25, 30, 28, 35],
    "city": ["Madrid", "Barcelona", "Valencia", "Madrid"],
})

# Filter: age >= 28
older = df[df["age"] >= 28]
print("Age >= 28:\n", older)

# Filter: city == "Madrid"
madrid = df[df["city"] == "Madrid"]
print("\nCity Madrid:\n", madrid)

# Combined: (age >= 28) AND (city == "Madrid")
filtered = df[(df["age"] >= 28) & (df["city"] == "Madrid")]
print("\nAge >= 28 and Madrid:\n", filtered)
