# -------------------------------------------------
# File Name: 27_comp_cond_vals.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Conditional values in comprehension with ternary operator.
# -------------------------------------------------

print("8. Conditional Values in Comprehension:")
print("-" * 60)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Classify each number as "even" or "odd" based on modulo
# Ternary syntax: value_if_true if condition else value_if_false
number_types = {
    num: "even" if num % 2 == 0 else "odd"
    for num in numbers
}
print(f"Number classifications: {number_types}")
