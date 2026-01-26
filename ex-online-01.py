'''
Author: Florentino Baez
date: 1/15/26
subject: first week of python
Description: This program calculates the area of a circle given a radius.
variables rules:
- Variable names must start with a letter or underscore (_)
- Variable names can only contain alphanumeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- Variable names cannot be a reserved keyword in Python (like print, for, if, else, etc.)
'''
import math
# example 01
print("*" * 30)
print("Hello this the first evening class")
print("It starts at 6 p.m.")
print("*" * 30)

# formula for calculate area of circle (circle area using radius)
print("*" * 30)
print("Area of Circle")
print("Using radius 20")
print("*" * 30)

# variable for radius and pi
student_name = "Florentino Baez"
hair_color = "Black"
radius = 20
pi = math.pi

# calculate area
area = radius * radius * pi
print(f"{student_name},your hair color is {hair_color} and the area for the Circle of radius {radius} is: {area}")

# example 02
print("*" * 30)
# operators
print("Operators")
a = 10
b = 3
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b
print(f"Addition: {a} + {b} = {addition}")
print(f"Subtraction: {a} - {b} = {subtraction}")
print(f"Multiplication: {a} * {b} = {multiplication}")
print(f"Division: {a} / {b} = {division}")
print(f"Modulus: {a} % {b} = {modulus}")
print("*" * 30)

# example 03
# whasping variables
print("Whasping Variables")
x = 5
print(f"Initial value of x: {x}")
x += 3  # Equivalent to x = x + 3
print(f"After x += 3: {x}")
x *= 2  # Equivalent to x = x * 2
print(f"After x *= 2: {x}")
y = 10
print(f"Initial value of y: {y}")
x, y = y, x  # Swapping values
print(f"After swapping, x: {x}, y: {y}")
print("*" * 30)

# integer division
print("Integer Division")
num1 = 15
num2 = 4
int_division = num1 // num2
print(f"Integer Division: {num1} // {num2} = {int_division}")
print("*" * 30)

# module operator
print("Module Operator")
num3 = 29
num4 = 5
mod_result = num3 % num4
print(f"Module Operator: {num3} % {num4} = {mod_result}")
print("*" * 30)

# example 04
# augmented assignment operators
print("Augmented Assignment Operators")
value = 10
print(f"Initial value: {value}")
value += 5  # Equivalent to value = value + 5
print(f"After += 5: {value}")
value -= 3  # Equivalent to value = value - 3
print(f"After -= 3: {value}")
value *= 2  # Equivalent to value = value * 2
print(f"After *= 2: {value}")
value /= 4  # Equivalent to value = value / 4
print(f"After /= 4: {value}")
print("*" * 30)

# another example with whasping variables
print("Another Example with Whasping Variables")
shoes = 50
hats = 30
print(f"Initial values - Shoes: {shoes}, Hats: {hats}")
shoes, hats = hats, shoes  # Swapping values
print(f"After swapping - Shoes: {shoes}, Hats: {hats}")
print("*" * 30)
