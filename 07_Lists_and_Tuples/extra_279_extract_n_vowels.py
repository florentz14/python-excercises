# 279. Extract First n Vowels from String

def extract_n_vowels(s: str, n: int) -> str:
    vowels = 'aeiouAEIOU'
    found = [c for c in s if c in vowels]
    if len(found) < n:
        return "n is less than number of vowels present in the string."
    return ''.join(found[:n])


print(extract_n_vowels("Python", 2))  # "n is less..."
print(extract_n_vowels("Python Exercises", 3))  # oEe
print(extract_n_vowels("aeiou", 3))  # aei
