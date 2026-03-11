# -------------------------------------------------
# File Name: 30_strings_and_advanced_groupby.py
# Author: Florentino Baez
# Date: 09_Pandas
# Description: String cleanup, regex, transform, and apply.
# -------------------------------------------------

import re

import pandas as pd

# 1. String manipulation and regex
text = "foo,  bar, \t baz,  qux"
pieces = [value.strip() for value in text.split(",")]
print("=== CLEANED PIECES ===")
print(pieces)

# Create a regex for the email
email_regex = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}", flags=re.IGNORECASE)
# Create a sample with the email
sample = "Contact us at data.team@example.com or admin@company.org"
# Find the emails in the sample
emails = email_regex.findall(sample)

print("\n=== REGEX EMAIL MATCHES ===")
print(emails)

# 2. Aggregation with transform and apply
df = pd.DataFrame({"key": ["A", "B", "C", "A", "B", "C"], "data": range(6)})

# Create a new column with the sum of the data for each key
group_sum = df.groupby("key")["data"].transform("sum")
df["total_for_key"] = group_sum

print("\n=== TRANSFORM RESULT ===")
print(df)

# Create a new column with the max of the data for each key
result = df.groupby("key").apply(lambda group: group.max(), include_groups=False)
print("\n=== APPLY RESULT (MAX BY GROUP) ===")
print(result)
