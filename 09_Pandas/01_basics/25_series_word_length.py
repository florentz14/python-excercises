# -------------------------------------------------
# File Name: 25_series_word_length.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Counts characters of words in a pandas Series.
# -------------------------------------------------

import pandas as pd

# Create a Pandas Series of words
series = pd.Series(
    ["Php", "Python", "Java", "C#", "C++", "JavaScript", "Swift", "Kotlin", "Rust", "Go"]
)

print("=" * 40)
print("     WORD CHARACTER COUNT")
print("=" * 40)
print("Original Series:")
print(series.to_string())
print("=" * 40)

# Character Count using .str.len()
char_count = series.str.len()
print("\nCharacter Count per Word:")
print(char_count.to_string())

# Display Word alongside its Length
print("\n-- Word -> Character Count --------")
for word, count in zip(series, char_count):
    bar = "#" * count
    print(f"  {word:<12} ->  {count:>2}  {bar}")

# Statistical Summary of Lengths
print("\n-- Length Statistics --------------")
print(f"  Shortest Word Length : {char_count.min()}")
print(f"  Longest  Word Length : {char_count.max()}")
print(f"  Average  Word Length : {char_count.mean():.2f}")
print(f"  Total    Characters  : {char_count.sum()}")

# Shortest & Longest Words
print("\n-- Shortest and Longest Words -----")
print(f"  Shortest : {series[char_count.idxmin()]} ({char_count.min()} chars)")
print(f"  Longest  : {series[char_count.idxmax()]} ({char_count.max()} chars)")

# Filter Words by Length
print("\n-- Words with Length <= 4 ---------")
short_words = series[char_count <= 4]
print(f"  {short_words.tolist()}")

print("\n-- Words with Length >= 6 ---------")
long_words = series[char_count >= 6]
print(f"  {long_words.tolist()}")

# Group Words by Length
print("\n-- Words Grouped by Length --------")
result_df = pd.DataFrame({"Word": series, "Length": char_count})
grouped = result_df.groupby("Length")["Word"].apply(list)
for length, words in grouped.items():
    print(f"  {length} chars : {words}")

# Summary DataFrame
print("\n-- Summary DataFrame --------------")
summary_df = pd.DataFrame(
    {
        "Word": series.values,
        "Length": char_count.values,
        "Uppercase": series.str.upper().values,
        "Lowercase": series.str.lower().values,
    }
)
print(summary_df.to_string(index=False))
print("=" * 40)
