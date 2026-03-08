# -------------------------------------------------
# File Name: 36_division_error.py
# Description: Divide two numbers, error if divisor is zero
# -------------------------------------------------

a = float(input("Enter dividend: "))
b = float(input("Enter divisor: "))
if b == 0:
    print("Error: cannot divide by zero.")
else:
    print(f"Result: {a / b}")
