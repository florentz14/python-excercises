# -------------------------------------------------
# File Name: 02_ocean_levels.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming 
# Professor: Mauricio Quiroga
# Date: Module 04 Lab
# Description: Assuming the ocean's level is currently rising at about 1.6 
#              millimeters per year, write a program that displays a table 
#              showing the number of millimeters that the ocean will have risen 
#              each year for the next 25 years.
# -------------------------------------------------

print("=" * 60)
print("EXERCISE 2: Ocean Levels")
print("=" * 60)

# Constants
RISE_RATE = 1.6  # millimeters per year
YEARS_TO_DISPLAY = 25

print(f"Assuming the ocean's level is rising at {RISE_RATE} millimeters per year:")
print(f"\nYear\t\tOcean Level Rise (mm)")
print("-" * 40)

# Loop: Iterate through each year from 1 to 25
for year in range(1, YEARS_TO_DISPLAY + 1):
    total_rise = RISE_RATE * year
    print(f"{year}\t\t{total_rise:.1f}")

print(f"\nAfter {YEARS_TO_DISPLAY} years, the ocean will have risen {RISE_RATE * YEARS_TO_DISPLAY:.1f} millimeters.")

