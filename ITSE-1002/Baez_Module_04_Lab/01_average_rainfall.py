# -------------------------------------------------
# File Name: 01_average_rainfall.py
# Author: Florentino Báez
# Date: Baez_Module_04_Lab
# Description: Write a program that uses nested loops to collect data and
# -------------------------------------------------

print("=" * 60)
print("EXERCISE 1: Average Rainfall")
print("=" * 60)

# Month names
months = ["", "January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

# Get number of years
num_years = int(input("Enter the number of years: "))

# Initialize variables
total_rainfall = 0.0
total_months = 0

# Outer loop: for each year
for year in range(1, num_years + 1):
    print(f"\nYear {year}:")
    # Inner loop: for each month (12 months in a year)
    for month in range(1, 13):
        rainfall = float(
            input(f"  Enter inches of rainfall for {months[month]}: "))
        total_rainfall += rainfall
        total_months += 1

# Calculate average
average_rainfall = total_rainfall / total_months

# Display results
print("\n" + "=" * 60)
print("RAINFALL SUMMARY")
print("=" * 60)
print(f"Number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")

