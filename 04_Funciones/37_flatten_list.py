# 37_flatten_list.py
# Function to flatten a nested list

def flatten_list(nested_list):
    """
    Recursively flattens a nested list of any depth.
    
    Args:
        nested_list: A list that may contain nested lists
        
    Returns:
        A flat list with all elements at the same level
    """
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened


def flatten_one_level(nested_list):
    """
    Flattens only one level of nesting.
    
    Args:
        nested_list: A list with nested lists
        
    Returns:
        A list flattened by one level
    """
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(item)
        else:
            flattened.append(item)
    return flattened


def get_depth(nested_list):
    """
    Returns the maximum depth of a nested list.
    
    Args:
        nested_list: A list that may contain nested lists
        
    Returns:
        Integer representing the maximum nesting depth
    """
    if not isinstance(nested_list, list):
        return 0
    if not nested_list:
        return 1
    return 1 + max(get_depth(item) for item in nested_list)


# Example usage
if __name__ == "__main__":
    print("=== Flatten Nested List Demo ===\n")
    
    # Test cases
    nested1 = [1, [2, 3], 4, [5, 6]]
    nested2 = [1, [2, [3, [4, [5]]]]]
    nested3 = [[1, 2], [3, 4], [5, 6]]
    nested4 = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
    
    print("1. Simple nesting:")
    print(f"   Original: {nested1}")
    print(f"   Flattened: {flatten_list(nested1)}")
    print()
    
    print("2. Deep nesting:")
    print(f"   Original: {nested2}")
    print(f"   Depth: {get_depth(nested2)}")
    print(f"   Flattened: {flatten_list(nested2)}")
    print()
    
    print("3. List of lists:")
    print(f"   Original: {nested3}")
    print(f"   Flattened: {flatten_list(nested3)}")
    print()
    
    print("4. Mixed nesting:")
    print(f"   Original: {nested4}")
    print(f"   Flattened: {flatten_list(nested4)}")
    print()
    
    print("5. One-level flatten comparison:")
    print(f"   Original: {nested4}")
    print(f"   One level: {flatten_one_level(nested4)}")
    print(f"   Full:      {flatten_list(nested4)}")
