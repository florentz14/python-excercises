# -------------------------------------------------
# File Name: 21_word_frequency.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Word Frequency Counter.
#              Builds a practical application that counts word
#              occurrences using a manual dict approach and
#              collections.Counter. Includes statistics, filtering,
#              character analysis, and product review analysis.
# -------------------------------------------------

"""
Exercise 5: Word Frequency Counter
This exercise builds a practical application that counts word occurrences in text.
This is a common use case for dictionaries in text processing and data analysis.
"""

from collections import Counter
import re


def count_words_manual(text):
    """
    Count word frequency manually using a dictionary.
    
    Args:
        text: Input text string
    
    Returns:
        Dictionary with word counts
    """
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Create frequency dictionary to store word counts
    word_count = {}
    for word in words:
        # Remove punctuation using regex (keep only word characters and whitespace)
        word = re.sub(r'[^\w\s]', '', word)
        if word:  # Skip empty strings after punctuation removal
            # Increment count for this word, defaulting to 0 if not seen before
            word_count[word] = word_count.get(word, 0) + 1
    
    return word_count


def count_words_counter(text):
    """
    Count word frequency using Counter from collections.
    
    Args:
        text: Input text string
    
    Returns:
        Counter object with word counts
    """
    # Clean and split text: find all word characters (alphanumeric + underscore)
    words = re.findall(r'\w+', text.lower())
    # Counter automatically counts occurrences of each word
    return Counter(words)


def main():
    print("Exercise 5: Word Frequency Counter")
    print("=" * 60)
    
    # Sample text
    text = """
    Python is an amazing programming language. Python is versatile
    and Python is easy to learn. Many developers love Python because
    Python has a simple syntax. Python is great for beginners.
    """
    
    print("Sample Text:")
    print("-" * 60)
    print(text.strip())
    print()
    
    # Method 1: Manual counting with dictionary
    print("Method 1: Manual Dictionary Approach")
    print("-" * 60)
    manual_count = count_words_manual(text)
    
    # Sort by frequency (descending): key=lambda x: x[1] sorts by count value
    sorted_words = sorted(manual_count.items(), key=lambda x: x[1], reverse=True)
    
    print("Word frequencies:")
    # Display top 10 most frequent words
    for word, count in sorted_words[:10]:
        print(f"  {word:15} : {count:2} times")
    print()
    
    # Method 2: Using Counter
    print("Method 2: Using collections.Counter")
    print("-" * 60)
    counter_result = count_words_counter(text)
    
    print("Top 10 most common words:")
    for word, count in counter_result.most_common(10):
        print(f"  {word:15} : {count:2} times")
    print()
    
    # Calculate and display text statistics
    print("Statistics:")
    print("-" * 60)
    total_words = sum(manual_count.values())  # Sum all word counts
    unique_words = len(manual_count)  # Count distinct words
    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")
    print(f"Average frequency: {total_words/unique_words:.2f}")
    print()
    
    # Find words that appear only once (hapax legomena)
    print("Words appearing only once:")
    print("-" * 60)
    # List comprehension filters words with count == 1
    single_occurrence = [word for word, count in manual_count.items() if count == 1]
    print(f"Count: {len(single_occurrence)}")
    print(f"Words: {sorted(single_occurrence)}")
    print()
    
    # Filter dictionary to show only words meeting frequency threshold
    print("Filtering by Frequency:")
    print("-" * 60)
    # Dictionary comprehension: keep only words with count >= 3
    frequent_words = {word: count for word, count in manual_count.items() if count >= 3}
    print(f"Words appearing 3+ times: {frequent_words}")
    print()
    
    # Character frequency analysis (bonus feature)
    print("Bonus: Character Frequency Analysis")
    print("-" * 60)
    # Remove all whitespace characters and convert to lowercase
    chars = re.sub(r'\s', '', text.lower())
    char_count = Counter(chars)  # Count each character occurrence
    
    print("Top 5 most common characters:")
    # most_common(5) returns the 5 characters with highest counts
    for char, count in char_count.most_common(5):
        if char.isalpha():  # Only display alphabetic characters
            print(f"  '{char}' : {count} times")
    print()
    
    # Practical example: Analyzing user reviews
    print("Practical Example: Product Review Analysis")
    print("-" * 60)
    reviews = [
        "Great product, very satisfied!",
        "Amazing quality, highly recommend.",
        "Good product but shipping was slow.",
        "Great value for money, very happy.",
        "Product quality is amazing!"
    ]
    
    # Combine all reviews into a single text string
    all_reviews = " ".join(reviews)
    review_words = count_words_counter(all_reviews)
    
    print("Most mentioned words in reviews:")
    # Display top 8 words, filtering out short words (likely articles/prepositions)
    for word, count in review_words.most_common(8):
        if len(word) > 3:  # Skip short words like "the", "is", "was"
            print(f"  {word:12} : {count} times")
    
    print("\n" + "=" * 60)
    print("Key Takeaways:")
    print("  - Dictionaries are perfect for counting occurrences")
    print("  - Use dict.get(key, 0) + 1 for counting")
    print("  - collections.Counter simplifies frequency analysis")
    print("  - Sort with sorted() and lambda for ordered results")
    print("  - Useful for text analysis, log processing, etc.")


if __name__ == "__main__":
    main()
