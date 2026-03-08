# -------------------------------------------------
# File Name: 29_is_palindrome.py
# Author: Florentino Báez
# Date: 04_Functions
# Description: Palindrome checker function.
# -------------------------------------------------

def is_palindrome(word):
    """
    Checks if a word reads the same forwards and backwards.
    
    Args:
        word: A string to check
        
    Returns:
        True if the word is a palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase for comparison
    clean_word = word.lower().replace(" ", "")
    return clean_word == clean_word[::-1]


# Example usage
if __name__ == "__main__":
    print("=== Palindrome Checker Demo ===\n")
    
    # Test words
    test_words = [
        "radar",
        "level",
        "hello",
        "A man a plan a canal Panama",
        "racecar",
        "python",
        "madam",
        "noon"
    ]
    
    for word in test_words:
        result = is_palindrome(word)
        status = "YES" if result else "NO"
        print(f"'{word}' -> {status}")
