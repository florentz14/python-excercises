import pandas as pd


series = pd.Series(
    ["Php", "Python", "Java", "C#", "C++", "JavaScript", "Swift", "Kotlin", "Rust", "Go"]
)
char_count = series.str.len()

print("Length Statistics:")
print(f"Shortest Word Length : {char_count.min()}")
print(f"Longest  Word Length : {char_count.max()}")
print(f"Average  Word Length : {char_count.mean():.2f}")
print(f"Total    Characters  : {char_count.sum()}")

print("\nShortest and Longest Words:")
print(f"Shortest : {series[char_count.idxmin()]} ({char_count.min()} chars)")
print(f"Longest  : {series[char_count.idxmax()]} ({char_count.max()} chars)")

short_words = series[char_count <= 4]
long_words = series[char_count >= 6]
print(f"\nWords with Length <= 4: {short_words.tolist()}")
print(f"Words with Length >= 6: {long_words.tolist()}")
