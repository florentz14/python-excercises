# Exercise 2: Adding Spacing for Alignment
# Use f-strings with left-alignment formatting (:<) to create neatly
# aligned columns with consistent spacing.

# Create variables for numbers 1 to 9
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
num6 = 6
num7 = 7
num8 = 8
num9 = 9

# Same numbers but aligned neatly with spaces using f-strings
print("Exercise 2: Adding Spacing for Alignment")
print("-" * 20)
print(f"{num1:<5}{num2:<5}{num3:<5}")
print(f"{num4:<5}{num5:<5}{num6:<5}")
print(f"{num7:<5}{num8:<5}{num9:<5}")

# Explanation
print("\nExplanation:")
print("The format '<5' means: left-align the value in a field of width 5")
print("This creates neat columns with consistent spacing")
