# -------------------------------------------------
# File Name: 62_for_print_temperatures.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Date: Module 04 Lab (added)
# Description: Simple for-loop example — print temperatures from a list.
# -------------------------------------------------

print("=" * 40)
print("For #1 – Print Temperatures")
print("=" * 40)

# List of temperatures in Fahrenheit
temps = [72, 68, 75]

# Loop: iterate over each temperature and print formatted output
for t in temps:
    print("Temp:", str(t) + "°F")

print("=" * 40)
