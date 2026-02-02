# 114. Extract n-th Element from List of Tuples

def extract_nth(tuples: list[tuple], n: int) -> list:
    return [t[n] for t in tuples if len(t) > n]


sample = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96)]
print(extract_nth(sample, 0))  # names
print(extract_nth(sample, 2))  # [99, 96]
