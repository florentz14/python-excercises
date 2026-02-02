# 40. Split List by First Character of Word

from itertools import groupby

def split_by_first_char(words: list[str]) -> dict[str, list[str]]:
    sorted_words = sorted(words, key=lambda w: w[0] if w else '')
    return {k: list(g) for k, g in groupby(sorted_words, key=lambda w: w[0] if w else '')}


# Simpler: group by first char
words = ['apple', 'ant', 'dog', 'date']
result = {}
for w in words:
    key = w[0]
    result.setdefault(key, []).append(w)
print(result)
