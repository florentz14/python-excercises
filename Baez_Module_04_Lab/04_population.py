# -------------------------------------------------
# File Name: 04_population.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming 
# Professor: Mauricio Quiroga
# Date: Module 04 Lab
# Description: Write a program that predicts the approximate size of a 
#              population of organisms. The application should allow the user 
#              to enter the starting number of organisms, the average daily 
#              population increase (as a percentage), and the number of days 
#              the organisms will be left to multiply. The program should 
#              display a table showing the day number and the population at 
#              the beginning of that day.
#              Example:
#              - Starting number of organisms: 2
#              - Average daily increase: 30%
#              - Number of days to multiply: 10
# -------------------------------------------------

print("=" * 60)
print("EXERCISE 4: Population")
print("=" * 60)

# Get user input
starting_population = float(input("Enter the starting number of organisms: "))
daily_increase = float(input("Enter the average daily population increase (as a percentage): "))
num_days = int(input("Enter the number of days the organisms will be left to multiply: "))

# Convert percentage to decimal
increase_rate = daily_increase / 100

# Calculate and display population for each day
print(f"\nDay\t\tPopulation")
print("-" * 40)

population = starting_population
print(f"0\t\t{population:,.2f}")

# Loop: Iterate through each day to calculate population growth
for day in range(1, num_days + 1):
    population = population * (1 + increase_rate)
    print(f"{day}\t\t{population:,.2f}")

print(f"\nStarting population: {starting_population:,.2f}")
print(f"Daily increase: {daily_increase}%")
print(f"Final population after {num_days} days: {population:,.2f}")

