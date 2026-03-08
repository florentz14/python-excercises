# -------------------------------------------------
# File Name: 54_phrase_word_lengths.py
# Description: Return dict of words and their lengths
# -------------------------------------------------


def phrase_word_lengths(s: str) -> dict[str, int]:
    """Return {word: length} for each word in phrase."""
    return {w: len(w) for w in s.split()}


if __name__ == "__main__":
    print(phrase_word_lengths("hello world"))
    print(phrase_word_lengths("the quick brown fox"))
