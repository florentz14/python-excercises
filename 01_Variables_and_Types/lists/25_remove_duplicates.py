# eliminar duplicados

def remove_duplicates(lst):
    return list(set(lst))

# Or using dict.fromkeys to preserve order
def remove_duplicates_preserve_order(lst):
    return list(dict.fromkeys(lst))

original = [1, 2, 2, 3, 4, 4, 5]
print("Original:", original)
print("Without duplicates (set):", remove_duplicates(original))
print("Without duplicates (preserve order):", remove_duplicates_preserve_order(original))