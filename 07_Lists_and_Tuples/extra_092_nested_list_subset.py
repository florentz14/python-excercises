# 92. Check if Nested List Is Subset of Another

def nested_subset(a: list, b: list) -> bool:
    """Check if b is subset of a (all elements of b in a)."""
    for elem in b:
        if elem not in a:
            return False
    return True


print(nested_subset([[1, 3], [5, 7], [9, 11]], [[1, 3], [9, 11]]))  # True
