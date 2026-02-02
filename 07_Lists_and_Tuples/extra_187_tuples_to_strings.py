# 187. Convert List of Tuples to List of Strings (join with space)

def tuples_to_strings(tuples: list[tuple]) -> list[str]:
    return [' '.join(str(x) for x in t) for t in tuples]


sample = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
print(tuples_to_strings(sample))  # ['red green', 'black white', 'orange pink']
