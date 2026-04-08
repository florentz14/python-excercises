import pandas as pd


series = pd.Series(
    ["Php", "Python", "Java", "C#", "C++", "JavaScript", "Swift", "Kotlin", "Rust", "Go"]
)
char_count = series.str.len()

print("Original Series:")
print(series.to_string())
print("\nCharacter Count per Word:")
print(char_count.to_string())
