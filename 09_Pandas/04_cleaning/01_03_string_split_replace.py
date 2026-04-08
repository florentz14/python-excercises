import pandas as pd


df = pd.DataFrame(
    {
        "name": ["Anna Pérez", "bob SMITH", "Carol García", "DAVID Lee"],
        "email": ["anna@mail.com", "bob@work.org", "carol@home.net", "david@co.uk"],
        "phone": ["555-1234", "555.5678", "555 9012", "(555)3456"],
    }
)

df["name_clean"] = df["name"].str.strip().str.title()
df[["first", "last"]] = df["name_clean"].str.split(" ", n=1, expand=True)
df["phone_digits"] = df["phone"].str.replace(r"\D", "", regex=True)

print("Split first/last name:")
print(df[["name_clean", "first", "last"]])
print("\nPhone digits only:")
print(df[["phone", "phone_digits"]])
