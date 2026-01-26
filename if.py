# Simple If Conditional Program
# This program demonstrates basic if, elif, and else statements

# Example 1: Check if a number is positive, negative, or zero
print("Example 1: Number Classification")
print("-" * 40)
number = 15

if number > 0:
    print(f"{number} is a positive number")
elif number < 0:
    print(f"{number} is a negative number")
else:
    print(f"{number} is zero")

# Example 2: Check if a person can vote based on age
print("\nExample 2: Voting Eligibility")
print("-" * 40)
age = 20

if age >= 18:
    print(f"You are {age} years old. You can vote!")
else:
    print(f"You are {age} years old. You cannot vote yet.")

# Example 3: Grade assignment based on score
print("\nExample 3: Grade Assignment")
print("-" * 40)
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Example 4: Check if a number is even or odd
print("\nExample 4: Even or Odd")
print("-" * 40)
num = 42

if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

# Example 5: Simple login check
print("\nExample 5: Login Check")
print("-" * 40)
username = "admin"
password = "password123"

if username == "admin" and password == "password123":
    print("Login successful!")
else:
    print("Invalid username or password")
