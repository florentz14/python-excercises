# -------------------------------------------------
# File Name: 04_comparison.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Comparison operators (==, !=, <, >, <=, >=) compare
# -------------------------------------------------

a = 10
b = 5

print("a =", a, ", b =", b)
print("a == b (equal):", a == b)
print("a != b (not equal):", a != b)
print("a < b (less than):", a < b)
print("a > b (greater than):", a > b)
print("a <= b (less or equal):", a <= b)
print("a >= b (greater or equal):", a >= b)

# String comparisons (lexicographic order)
s1 = "abc"
s2 = "abd"
print("\nStrings: s1 =", s1, ", s2 =", s2)
print("s1 < s2:", s1 < s2)

# Chained comparisons
x = 5
print("\n1 < x < 10:", 1 < x < 10)
print("1 < x < 3:", 1 < x < 3)
