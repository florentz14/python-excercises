# dividir listas (chunk list)

def chunk_list(lst, chunk_size):
    """Split list into chunks of given size."""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original:", original)
print("Chunks of 3:", chunk_list(original, 3))
print("Chunks of 4:", chunk_list(original, 4))
