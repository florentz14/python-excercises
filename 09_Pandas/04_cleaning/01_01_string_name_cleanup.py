import pandas as pd


df = pd.DataFrame(
    {
        "name": ["Anna Pérez", "bob SMITH", "Carol García", "DAVID Lee"],
        "email": ["anna@mail.com", "bob@work.org", "carol@home.net", "david@co.uk"],
        "phone": ["555-1234", "555.5678", "555 9012", "(555)3456"],
    }
)

df["name_clean"] = df["name"].str.strip().str.title()

print("Name cleanup with strip/title:")
print(df[["name", "name_clean"]])
