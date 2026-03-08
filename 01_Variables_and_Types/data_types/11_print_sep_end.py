# -------------------------------------------------
# File Name: 11_print_sep_end.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Controlling print(): sep (separator between arguments)
# -------------------------------------------------

print(1, 2, 3)
print(1, 2, 3, sep="-")
print(1, 2, 3, sep=", ")
print("a", "b", "c", sep="")

# end: what to print at the end (default: \n)
print("No newline", end="")
print(" here")
print("Line 1", end=" | ")
print("Line 2", end=" | ")
print("Line 3")

# Combine sep and end
print(10, 20, 30, sep=" + ", end=" = ")
print(60)
