# -------------------------------------------------
# File Name: exercise_bmi.py
# Author: Florentino Báez
# Date: Baez_Module_03_Lab
# Description: Body Mass Index (BMI)
# -------------------------------------------------

print("=" * 60)
print("EXERCISE 4: Body Mass Index (BMI)")
print("=" * 60)

# Get user input
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

# Validate inputs
if weight <= 0 or height <= 0:
    print("Error: Weight and height must be positive numbers.")
else:
    # Calculate BMI
    # Formula: BMI = weight x 703 / height^2
    bmi = (weight * 703) / (height ** 2)

    # Determine weight status
    if bmi < 18.5:
        status = "underweight"
    elif 18.5 <= bmi <= 25:
        status = "optimal weight"
    else:  # bmi > 25
        status = "overweight"

    # Display results
    print(f"\nYour BMI: {bmi:.2f}")
    print(f"Weight Status: You have {status}.")

    # Display BMI ranges for reference
    print("\nBMI Ranges:")
    print("  Less than 18.5  - Underweight")
    print("  18.5 to 25      - Optimal weight")
    print("  Greater than 25 - Overweight")

print("\n" + "=" * 60)
print("Exercise completed!")
print("=" * 60)
