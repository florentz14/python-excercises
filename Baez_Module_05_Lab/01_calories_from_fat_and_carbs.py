#!/usr/bin/env python3
# -------------------------------------------------
# File Name: 01_calories_from_fat_and_carbs.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: Module 05 Lab
# Description: Calculate calories from fat and carbohydrates.
# -------------------------------------------------

"""Baez Module 05 Lab - Exercise 1
Calories from Fat and Carbohydrates
"""


def calculate_calories_from_fat(fat_grams: float) -> float:
    """Return calories from fat (fat_grams * 9)."""
    return fat_grams * 9


def calculate_calories_from_carbs(carb_grams: float) -> float:
    """Return calories from carbohydrates (carb_grams * 4)."""
    return carb_grams * 4


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 1: Calories from Fat and Carbohydrates")
    print("=" * 60)
    try:
        fat_grams = float(input("Enter the number of fat grams consumed: "))
        carb_grams = float(
            input("Enter the number of carbohydrate grams consumed: "))
        if fat_grams < 0 or carb_grams < 0:
            print("Error: Fat grams and carbohydrate grams must be non-negative.")
        else:
            calories_from_fat = calculate_calories_from_fat(fat_grams)
            calories_from_carbs = calculate_calories_from_carbs(carb_grams)
            total_calories = calories_from_fat + calories_from_carbs
            print(f"\nCalories from fat: {calories_from_fat:.2f}")
            print(f"Calories from carbohydrates: {calories_from_carbs:.2f}")
            print(f"Total calories: {total_calories:.2f}")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"Error: {e}")

print()

print("\n" + "=" * 60)
print("CITATION")
print("=" * 60)
print("1. Calories Calculation:")
print("   - Fat: 1 gram of fat = 9 calories")
print("   - Carbohydrates: 1 gram of carbohydrates = 4 calories")
print("   Source: USDA National Nutrient Database")
print("   https://www.nal.usda.gov/fnic/how-many-calories-are-one-gram-fat-carbohydrate-or-protein")
