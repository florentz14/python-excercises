# -------------------------------------------------
# File Name: 60_string_methods.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: str.lower, str.contains, str.extract, str.split, str.replace.
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "name": ["Anna Pérez", "bob SMITH", "Carol García", "DAVID Lee"],
    "email": ["anna@mail.com", "bob@work.org", "carol@home.net", "david@co.uk"],
    "phone": ["555-1234", "555.5678", "555 9012", "(555)3456"],
})

print("=== ORIGINAL ===")
print(df)
print()

# str.lower, str.upper, str.strip
df["name_clean"] = df["name"].str.strip().str.title()
print("=== str.strip().str.title() ===")
print(df[["name", "name_clean"]])
print()

# str.contains (regex)
has_mail_work = df["email"].str.contains(r"@(?:mail|work)", case=False)
print("=== str.contains() — mail or work domain ===")
print(df.loc[has_mail_work, "email"].tolist())
print()

# str.extract (capture groups)
df["domain"] = df["email"].str.extract(r"@([\w.]+)", expand=False)
print("=== str.extract() — domain ===")
print(df[["email", "domain"]])
print()

# str.split
df[["first", "last"]] = df["name_clean"].str.split(" ", n=1, expand=True)
print("=== str.split() — first/last name ===")
print(df[["name_clean", "first", "last"]])
print()

# str.replace
df["phone_digits"] = df["phone"].str.replace(r"\D", "", regex=True)
print("=== str.replace() — digits only ===")
print(df[["phone", "phone_digits"]])
print()

# str.len
df["email_len"] = df["email"].str.len()
print("=== str.len() ===")
print(df[["email", "email_len"]])
