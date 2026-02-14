# -------------------------------------------------
# File Name: 01_calories_from_fat_and_carbs.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: Module 05 Lab
# Description: Calculate calories from fat and carbohydrates.
# -------------------------------------------------

# Calculate calories from fat (9 cal/gram)
def calculate_calories_from_fat(fat_grams: float) -> float:
    return fat_grams * 9


# Calculate calories from carbohydrates (4 cal/gram)
def calculate_calories_from_carbs(carb_grams: float) -> float:
    return carb_grams * 4


# Function: Main function to run the program
print("=" * 60)
print("EXERCISE 1: Calories from Fat and Carbohydrates")
print("=" * 60)

# Function: Get user input
fat_grams = float(input("Enter the number of fat grams consumed: "))
carb_grams = float(input("Enter the number of carbohydrate grams consumed: "))

if fat_grams < 0 or carb_grams < 0:
    print("Error: Fat grams and carbohydrate grams must be non-negative.")
else:
    calories_from_fat = calculate_calories_from_fat(fat_grams)
    calories_from_carbs = calculate_calories_from_carbs(carb_grams)
    total_calories = calories_from_fat + calories_from_carbs
    print(f"\nCalories from fat: {calories_from_fat:.2f}")
    print(f"Calories from carbohydrates: {calories_from_carbs:.2f}")
    print(f"Total calories: {total_calories:.2f}")

print()
