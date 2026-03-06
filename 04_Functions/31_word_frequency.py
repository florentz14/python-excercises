# -------------------------------------------------
# File: 31_word_frequency.py
# Description: Count word frequency in a text.
#              Dictionary operations and text processing.
# -------------------------------------------------

def word_frequency(text):
    """
    Returns a dictionary with the frequency of each word.
    
    Args:
        text: A string containing words
        
    Returns:
        A dictionary where keys are words and values are counts
    """
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def most_common_word(text):
    """
    Returns the most common word in the text.
    
    Args:
        text: A string containing words
        
    Returns:
        A tuple (word, count) of the most frequent word
    """
    freq = word_frequency(text)
    if not freq:
        return None
    return max(freq.items(), key=lambda x: x[1])


# Example usage
if __name__ == "__main__":
    print("=== Word Frequency Counter Demo ===\n")
    
    # Test text
    text = "hello world hello python world hello programming python"
    
    print(f"Text: '{text}'")
    print()
    
    # Get frequency
    freq = word_frequency(text)
    print("Word frequencies:")
    for word, count in sorted(freq.items()):
        print(f"  '{word}': {count}")
    
    print()
    
    # Most common word
    common = most_common_word(text)
    print(f"Most common word: '{common[0]}' (appears {common[1]} times)")
