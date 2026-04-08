import pandas as pd


series = pd.Series(
    ["Php", "Python", "Java", "C#", "C++", "JavaScript", "Swift", "Kotlin", "Rust", "Go"]
)
char_count = series.str.len()

result_df = pd.DataFrame({"Word": series, "Length": char_count})
grouped = result_df.groupby("Length")["Word"].apply(list)

print("Words Grouped by Length:")
for length, words in grouped.items():
    print(f"  {length} chars : {words}")

summary_df = pd.DataFrame(
    {
        "Word": series.values,
        "Length": char_count.values,
        "Uppercase": series.str.upper().values,
        "Lowercase": series.str.lower().values,
    }
)

print("\nSummary DataFrame:")
print(summary_df.to_string(index=False))
