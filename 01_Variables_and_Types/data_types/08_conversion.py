# -------------------------------------------------
# File Name: 08_conversion.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Type conversion: int(), float(), str(), bool(),
# -------------------------------------------------

print("--- Numeric conversion ---")
print("int(3.9):", int(3.9))      # Truncates decimals
print("float(7):", float(7))
print("int('42'):", int("42"))
print("float('3.14'):", float("3.14"))

# Conversion to string
print("\n--- Conversion to string ---")
print("str(100):", str(100))
print("str(3.14):", str(3.14))
print("str(True):", str(True))

# Conversion to bool (truthy/falsy values)
print("\n--- Conversion to bool ---")
print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool(''):", bool(""))
print("bool('text'):", bool("text"))
print("bool([]):", bool([]))
print("bool([1,2]):", bool([1, 2]))

# Conversion between sequences
print("\n--- Conversion between sequences ---")
lst = [1, 2, 3]
tpl = tuple(lst)
print("tuple([1,2,3]):", tpl)

s = "abc"
list_chars = list(s)  # string to list of chars
print("list('abc'):", list_chars)

st = set([1, 2, 2, 3])  # list to set (removes duplicates)
print("set([1,2,2,3]):", st)
