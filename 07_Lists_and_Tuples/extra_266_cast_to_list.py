# 266. Cast Value to List If Not Already

def ensure_list(x) -> list:
    if isinstance(x, list):
        return x
    return list(x) if hasattr(x, '__iter__') and not isinstance(x, str) else [x]


print(type(ensure_list(1)), ensure_list(1))       # list [1]
print(ensure_list((1, 2, 3)))   # [1, 2, 3]
print(ensure_list("hi"))        # ['h', 'i'] or [x] for single; often [x] for str
# Sample: "Red" -> ['R','e','d'], so list("Red")
print(ensure_list("Red"))       # ['R', 'e', 'd']
