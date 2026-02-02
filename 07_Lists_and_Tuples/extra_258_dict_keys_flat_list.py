# 258. Flat List of All Keys from Dictionary

def dict_keys_list(d: dict) -> list:
    return list(d.keys())


sample = {'Laura': 10, 'Spencer': 11, 'Bridget': 9}
print(dict_keys_list(sample))
