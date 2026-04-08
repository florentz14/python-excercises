import pandas as pd


df = pd.DataFrame(
    {
        "name": ["Anna Pérez", "bob SMITH", "Carol García", "DAVID Lee"],
        "email": ["anna@mail.com", "bob@work.org", "carol@home.net", "david@co.uk"],
        "phone": ["555-1234", "555.5678", "555 9012", "(555)3456"],
    }
)

df["email_len"] = df["email"].str.len()

print("Email length:")
print(df[["email", "email_len"]])
