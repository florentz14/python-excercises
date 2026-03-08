# -------------------------------------------------
# File Name: 20_table_print_end_parameter.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Use print(end=) to control line breaks and print
# -------------------------------------------------

print("Exercise 5: Printing a Table with end parameter")
print("-" * 40)

# Printing on the same line using end=""
print("1", end=" ")
print("2", end=" ")
print("3")
print("4", end=" ")
print("5", end=" ")
print("6")
print("7", end=" ")
print("8", end=" ")
print("9")

print("\nExplanation:")
print("- end=' ' makes print() add a space instead of a newline")
print("- Without end parameter, print() adds a newline by default")
print("- This allows you to print multiple values on the same line")
