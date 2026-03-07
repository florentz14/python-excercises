# Hashable vs unhashable keys

# Hashable types (can be dictionary keys)
hashable_keys = {
    "string": "value",
    42: "number",
    (1, 2, 3): "tuple",  # tuples are hashable if all elements are
    True: "boolean",
    None: "none",
    frozenset([1, 2, 3]): "frozenset"
}

print("Hashable keys work:")
for key, value in hashable_keys.items():
    print(f"  {key} ({type(key).__name__}): {value}")

# Unhashable types (cannot be dictionary keys)
print("\nUnhashable types cause TypeError:")

try:
    bad_dict = {[1, 2, 3]: "list"}  # type: ignore  # lists are unhashable
except TypeError as e:
    print(f"  List as key: {e}")

try:
    bad_dict = {{'a': 1}: "dict"}  # type: ignore  # dicts are unhashable
except TypeError as e:
    print(f"  Dict as key: {e}")

try:
    bad_dict = {{1, 2, 3}: "set"}  # type: ignore  # sets are unhashable
except TypeError as e:
    print(f"  Set as key: {e}")

# Tuples with unhashable elements
try:
    bad_dict = {(1, [2, 3]): "tuple with list"}  # tuple containing list
except TypeError as e:
    print(f"  Tuple with list: {e}")

# What makes something hashable?
print("\nHashable check:")
print(f"  String: {hash('hello')}")
print(f"  List: unhashable")
print(f"  Tuple: {hash((1, 2, 3))}")

# Custom hashable objects


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


point_dict = {Point(1, 2): "origin", Point(3, 4): "other"}
print(f"\nCustom hashable objects: {point_dict}")
