# -------------------------------------------------
# File Name: 31_comp_nested.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Nested dict comprehension: outer keys, inner nested dicts.
# -------------------------------------------------

print("7. Nested Dictionary Comprehension:")
print("-" * 60)
# Create multiplication table: each key maps to a dict of its multiples
mult_table = {
    i: {j: i * j for j in range(1, 4)}
    for i in range(1, 4)
}
print("Multiplication table (1-3):")
for key, value in mult_table.items():
    print(f"  {key}: {value}")
