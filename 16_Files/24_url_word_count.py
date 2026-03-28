# -------------------------------------------------
# File Name: 24_url_word_count.py
# Created: 2026-03-08
# Description: Fetch file from URL and count words
# -------------------------------------------------

import urllib.request


def count_words_in_url(url: str) -> int:
    """Fetches content from URL and returns word count."""
    with urllib.request.urlopen(url) as response:
        text = response.read().decode("utf-8")
    return len(text.split())


if __name__ == "__main__":
    url = input("Enter URL: ").strip() or "https://www.python.org/"
    try:
        count = count_words_in_url(url)
        print(f"Number of words: {count}")
    except Exception as e:
        print(f"Error: {e}")
