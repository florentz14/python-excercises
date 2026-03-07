# Percentage Calculations in Python

def calculate_percentage(part, whole):
    """Calculate what percentage part is of whole"""
    if whole == 0:
        return "Error: Division by zero"
    return (part / whole) * 100


def calculate_part(percentage, whole):
    """Calculate part from percentage and whole"""
    return (percentage / 100) * whole


def calculate_whole(part, percentage):
    """Calculate whole from part and percentage"""
    if percentage == 0:
        return "Error: Division by zero"
    return (part / percentage) * 100


# Examples
print("Percentage Calculations:")
print("=" * 30)

# What percentage is 25 of 100?
print(f"25 is {calculate_percentage(25, 100)}% of 100")

# What is 20% of 150?
print(f"20% of 150 = {calculate_part(20, 150)}")

# If 30 is 15% of what number?
print(f"If 30 is 15% of a number, the number is {calculate_whole(30, 15)}")

# Grade calculations
print("\nGrade Examples:")
score = 85
total = 100
percentage = calculate_percentage(score, total)
print(f"Score: {score}/{total} = {percentage}%")

# Discount calculations
print("\nDiscount Examples:")
original_price = 200
discount_percent = 15
discount_amount = calculate_part(discount_percent, original_price)
final_price = original_price - discount_amount
print(f"Original price: ${original_price}")
print(f"Discount: {discount_percent}% = ${discount_amount}")
print(f"Final price: ${final_price}")

# Tax calculations
print("\nTax Examples:")
subtotal = 100
tax_rate = 8.5
tax_amount = calculate_part(tax_rate, subtotal)
total = subtotal + tax_amount
print(f"Subtotal: ${subtotal}")
print(f"Tax ({tax_rate}%): ${tax_amount}")
print(f"Total: ${total}")

# Percentage increase/decrease
print("\nPercentage Change:")
old_value = 50
new_value = 75
increase = calculate_percentage(new_value - old_value, old_value)
print(f"Value increased from {old_value} to {new_value}: +{increase}%")

old_value = 100
new_value = 80
decrease = calculate_percentage(old_value - new_value, old_value)
print(f"Value decreased from {old_value} to {new_value}: -{decrease}%")
