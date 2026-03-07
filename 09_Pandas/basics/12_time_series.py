# ------------------------------------------------------------
# Basic case: Time series
# ------------------------------------------------------------

import pandas as pd

# Create DataFrame with dates
df = pd.DataFrame({
    "date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"],
    "value": [100, 105, 102, 110],
})
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

print("DataFrame with date index:\n", df)

# Percent change
df["pct_change"] = df["value"].pct_change()
print("\nPercent change:\n", df)

# Resample (group by month if more data)
# Example: daily data -> monthly mean
print("\nPeriod mean:", df["value"].mean())
