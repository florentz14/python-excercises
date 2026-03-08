# -------------------------------------------------
# File Name: 23_fromkeys.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Create dict with fromkeys(): keys from iterable, single default.
# -------------------------------------------------

keys = ['a', 'b', 'c']
dict1 = dict.fromkeys(keys)
print("Dict with None default:", dict1)

# Create dict with custom default value
dict2 = dict.fromkeys(keys, 0)
print("Dict with 0 default:", dict2)

# Create dict with list default (be careful - same list object!)
dict3 = dict.fromkeys(keys, [])
print("Dict with list default:", dict3)
dict3['a'].append(1)
print("After modifying one list:", dict3)  # All lists are the same object!

# Better way for mutable defaults
dict4 = {key: [] for key in keys}
print("Dict with separate lists:", dict4)
dict4['a'].append(1)
print("After modifying one list:", dict4)
