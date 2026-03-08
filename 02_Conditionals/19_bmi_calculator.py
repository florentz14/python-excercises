# -------------------------------------------------
# File Name: 19_bmi_calculator.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Body Mass Index (BMI)
# -------------------------------------------------

print("=" * 60)
print("EXERCISE 4: Body Mass Index (BMI)")
print("=" * 60)

# Get user input
# Try-except block: Handles exceptions that may occur during input conversion
try:
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
            status = "underweight"  # Set status to "underweight" if BMI is less than 18.5
        elif 18.5 <= bmi <= 25:
            # Set status to "optimal weight" if BMI is between 18.5 and 25
            status = "optimal weight"
        else:  # bmi > 25
            status = "overweight"  # Set status to "overweight" if BMI is greater than 25

        # Display results
        print(f"\nYour BMI: {bmi:.2f}")
        print(f"Weight Status: You have {status}.")

        # Display BMI ranges for reference
        print("\nBMI Ranges:")  # Display BMI ranges for reference
        print("  Less than 18.5  - Underweight")  # Display Underweight range
        # Display Optimal weight range
        print("  18.5 to 25      - Optimal weight")
        print("  Greater than 25 - Overweight")  # Display Overweight range

except ValueError:
    # Handle invalid numeric input (e.g., non-numeric characters)
    print("Error: Please enter valid numbers.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()
print("=" * 60)
print("Exercise completed!")
print("=" * 60)

