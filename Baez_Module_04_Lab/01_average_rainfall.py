# -------------------------------------------------
# File Name: 01_average_rainfall.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: Module 04 Lab
# Description: Write a program that uses nested loops to collect data and
#              calculate the average rainfall over a period of years. The program
#              should first ask for the number of years. The outer loop will
#              iterate once for each year. The inner loop will iterate twelve
#              times, once for each month. Each iteration of the inner loop
#              will ask the user for the inches of rainfall for that month.
#              After all iterations, the program should display the number of
#              months, the total inches of rainfall, and the average rainfall
#              per month for the entire period.
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

