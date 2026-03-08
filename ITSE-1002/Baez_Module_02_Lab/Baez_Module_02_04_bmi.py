# -------------------------------------------------
# File Name: Baez_Module_02_04_bmi.py
# Author: Florentino Báez
# Date: Baez_Module_02_Lab
# Description: Demonstrates baez module 02 04 bmi.
# -------------------------------------------------

print("=" * 60)
print("EXERCISE 4: BMI Calculator (Extra Credit)")
print("=" * 60)

weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

bmi = (weight / (height ** 2)) * 703

if bmi < 18.5:
    classification = "Underweight"
elif 18.5 <= bmi < 25.0:
    classification = "Normal"
elif 25.0 <= bmi < 30.0:
    classification = "Overweight"
else:
    classification = "Obese"

print(f"\nYour BMI: {bmi:.2f}")
print(f"Weight Classification: {classification}")

print("\nBMI Classification Chart:")
print("  Below 18.5     - Underweight")
print("  18.5 - 24.9    - Normal")
print("  25.0 - 29.9    - Overweight")
print("  30.0 or higher - Obese")

print()
