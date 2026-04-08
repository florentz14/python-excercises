import pandas as pd


summary = pd.DataFrame(
    {
        "Function / Option": [
            "pd.merge(df1, df2)",
            'pd.merge(..., on="col")',
            'pd.merge(..., how="left")',
            'pd.merge(..., how="right")',
            'pd.merge(..., how="outer")',
            "df1.join(df2)",
            "df1.join([df2, df3])",
        ],
        "Description": [
            "Inner join; auto-detects common column(s)",
            "Inner join on explicit column key",
            "Keep all left rows",
            "Keep all right rows",
            "Keep all rows from both",
            "Index-based join",
            "Join multiple DataFrames by index",
        ],
    }
)

print("Merge/Join quick reference:")
print(summary.to_string(index=False))
