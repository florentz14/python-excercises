import pandas as pd


df = pd.DataFrame(
    {
        "name": ["Anna Pérez", "bob SMITH", "Carol García", "DAVID Lee"],
        "email": ["anna@mail.com", "bob@work.org", "carol@home.net", "david@co.uk"],
        "phone": ["555-1234", "555.5678", "555 9012", "(555)3456"],
    }
)

has_mail_work = df["email"].str.contains(r"@(?:mail|work)", case=False)
df["domain"] = df["email"].str.extract(r"@([\w.]+)", expand=False)

print("Emails with mail/work domains:")
print(df.loc[has_mail_work, "email"].tolist())
print("\nExtracted domains:")
print(df[["email", "domain"]])
