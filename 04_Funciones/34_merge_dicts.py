# 34_merge_dicts.py
# Function to merge and sort two dictionaries

def merge_dicts(dict1, dict2):
    """
    Merges two dictionaries and sorts by values in descending order.
    
    Args:
        dict1: First dictionary
        dict2: Second dictionary (overwrites dict1 keys if duplicated)
        
    Returns:
        A new dictionary merged and sorted by values (descending)
    """
    merged = {**dict1, **dict2}
    return dict(sorted(merged.items(), key=lambda x: x[1], reverse=True))


def merge_dicts_ascending(dict1, dict2):
    """
    Merges two dictionaries and sorts by values in ascending order.
    
    Args:
        dict1: First dictionary
        dict2: Second dictionary
        
    Returns:
        A new dictionary merged and sorted by values (ascending)
    """
    merged = {**dict1, **dict2}
    return dict(sorted(merged.items(), key=lambda x: x[1]))


def merge_dicts_by_key(dict1, dict2):
    """
    Merges two dictionaries and sorts alphabetically by keys.
    
    Args:
        dict1: First dictionary
        dict2: Second dictionary
        
    Returns:
        A new dictionary merged and sorted by keys
    """
    merged = {**dict1, **dict2}
    return dict(sorted(merged.items()))


# Example usage
if __name__ == "__main__":
    print("=== Merge Dictionaries Demo ===\n")
    
    # Sample dictionaries
    d1 = {'apple': 5, 'banana': 3, 'cherry': 8}
    d2 = {'date': 2, 'apple': 10, 'elderberry': 7}
    
    print(f"Dictionary 1: {d1}")
    print(f"Dictionary 2: {d2}")
    print()
    
    # Merge with different sorting options
    print(f"Merged (by value desc): {merge_dicts(d1, d2)}")
    print(f"Merged (by value asc):  {merge_dicts_ascending(d1, d2)}")
    print(f"Merged (by key):        {merge_dicts_by_key(d1, d2)}")
    print()
    
    # Note about key conflicts
    print("Note: When keys conflict, dict2 values overwrite dict1")
    print(f"  'apple' was 5 in d1, but became 10 from d2")
