# -------------------------------------------------
# File Name: 37_real_world_filtering.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Real-world set filtering: students in math but not science;
# -------------------------------------------------

print("Real-World Set Filtering")
print("-" * 40)

# Example 1: Students in math but not science
math_students = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
science_students = {"Bob", "Diana", "Frank", "Grace"}

math_only = math_students - science_students
print("Math students:", math_students)
print("Science students:", science_students)
print("In math but NOT science:", math_only)
print()

# Example 2: Customers who bought both product A and B
bought_A = {"cust1", "cust2", "cust3", "cust4"}
bought_B = {"cust2", "cust4", "cust5", "cust6"}

bought_both = bought_A & bought_B
print("Bought A:", bought_A)
print("Bought B:", bought_B)
print("Bought BOTH A and B:", bought_both)
print()

# Bonus: bought A or B (union), bought A but not B
bought_either = bought_A | bought_B
bought_A_not_B = bought_A - bought_B
print("Bought A or B:", bought_either)
print("Bought A but not B:", bought_A_not_B)
