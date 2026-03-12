# -------------------------------------------------
# File Name: 48_strings_and_advanced_groupby.py
# Author: Florentino Baez
# Date: 12/03/2026
# Description: String cleanup, regex, transform, and apply.
# -------------------------------------------------

# Import re and pandas libraries
import re
import pandas as pd

# String manipulation and regex
text = "foo,  bar, \t baz,  qux"

# Split the text into pieces
pieces = [value.strip() for value in text.split(",")]
print("=== CLEANED PIECES ===")
print(pieces)

# Create a regex for the email
email_regex = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}", flags=re.IGNORECASE)

# Create a sample text containing emails
sample = "Contact us at data.team@example.com or admin@company.org"

# Find the emails in the sample text
emails = email_regex.findall(sample)

# Print the emails found
print("\n=== REGEX EMAIL MATCHES ===")
print(emails)

# Aggregation with transform and apply
df = pd.DataFrame({"key": ["A", "B", "C", "A", "B", "C"], "data": range(6)})

# Group by the key and apply the sum function
group_sum = df.groupby("key")["data"].transform("sum")

# Create a new column with the sum of the data for each key
df["total_for_key"] = group_sum

# Print the transformed DataFrame
print("\n=== TRANSFORM RESULT ===")
print(df)
