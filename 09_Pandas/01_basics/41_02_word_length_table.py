import pandas as pd


series = pd.Series(
    ["Php", "Python", "Java", "C#", "C++", "JavaScript", "Swift", "Kotlin", "Rust", "Go"]
)
char_count = series.str.len()

print("Word -> Character Count:")
for word, count in zip(series, char_count):
    bar = "#" * count
    print(f"  {word:<12} ->  {count:>2}  {bar}")
