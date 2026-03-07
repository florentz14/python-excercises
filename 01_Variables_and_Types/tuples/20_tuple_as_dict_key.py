# ------------------------------------------------------------
# File: 20_tuple_as_dict_key.py
# Purpose: Tuples as dictionary keys.
# Description: Hashable tuples can be keys; lists cannot.
# ------------------------------------------------------------

locations = {
    (10, 20): "Tree",
    (5, 7): "House",
    (0, 0): "Origin",
}

print("locations[(10,20)]:", locations[(10, 20)])
print("locations[(5,7)]:", locations[(5, 7)])

# Tuples are hashable; lists are not
# locations[[1,2]] = "Error"  # TypeError
