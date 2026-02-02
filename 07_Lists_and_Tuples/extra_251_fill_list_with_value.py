# 251. Fill List with Specified Value

def fill_list(value, length: int) -> list:
    return [value] * length


print(fill_list(0, 7))    # [0,0,0,0,0,0,0]
print(fill_list(3, 8))    # [3,3,...]
print(fill_list(3.2, 5))  # [3.2, ...]
