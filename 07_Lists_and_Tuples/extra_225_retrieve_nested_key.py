# 225. Retrieve Nested Key Value from Dict/List by Selector List

def get_nested(obj, selector: list):
    for key in selector:
        obj = obj[key]
    return obj


data = {'user': {'name': 'John', 'address': {'city': 'NYC'}}}
print(get_nested(data, ['user', 'name']))  # John
print(get_nested(data, ['user', 'address', 'city']))  # NYC
