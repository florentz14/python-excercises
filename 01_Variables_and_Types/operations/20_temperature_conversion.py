# -------------------------------------------------
# File Name: 20_temperature_conversion.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Celsius, Fahrenheit, and Kelvin conversion functions.
# -------------------------------------------------

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)


def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)


# Examples
print("Temperature Conversion:")
print("=" * 25)

# Water freezing and boiling points
print("Water freezing point:")
print(f"0°C = {celsius_to_fahrenheit(0)}°F = {celsius_to_kelvin(0)}K")

print("\nWater boiling point:")
print(f"100°C = {celsius_to_fahrenheit(100)}°F = {celsius_to_kelvin(100)}K")

# Room temperature
room_c = 25
print(f"\nRoom temperature ({room_c}°C):")
print(f"= {celsius_to_fahrenheit(room_c):.1f}°F")
print(f"= {celsius_to_kelvin(room_c):.2f}K")

# Body temperature
body_f = 98.6
body_c = fahrenheit_to_celsius(body_f)
body_k = fahrenheit_to_kelvin(body_f)
print(f"\nBody temperature ({body_f}°F):")
print(f"= {body_c:.1f}°C")
print(f"= {body_k:.2f}K")

# Absolute zero
abs_zero_k = 0
abs_zero_c = kelvin_to_celsius(abs_zero_k)
abs_zero_f = kelvin_to_fahrenheit(abs_zero_k)
print(f"\nAbsolute zero ({abs_zero_k}K):")
print(f"= {abs_zero_c}°C")
print(f"= {abs_zero_f:.2f}°F")

# Test conversions back and forth
test_temp = 37  # Body temperature in Celsius
fahrenheit = celsius_to_fahrenheit(test_temp)
back_to_celsius = fahrenheit_to_celsius(fahrenheit)
kelvin = celsius_to_kelvin(test_temp)
back_to_celsius_from_k = kelvin_to_celsius(kelvin)

print(f"\nConversion verification:")
print(f"Start: {test_temp}°C")
print(f"C -> F: {fahrenheit}°F")
print(f"F -> C: {back_to_celsius}°C")
print(f"C -> K: {kelvin}K")
print(f"K -> C: {back_to_celsius_from_k}°C")

# Temperature differences
print("\nTemperature differences:")
temp1_c = 20
temp2_c = 30
diff_c = temp2_c - temp1_c
diff_f = celsius_to_fahrenheit(temp2_c) - celsius_to_fahrenheit(temp1_c)
diff_k = celsius_to_kelvin(temp2_c) - celsius_to_kelvin(temp1_c)

print(f"Difference between {temp1_c}°C and {temp2_c}°C:")
print(f"In Celsius: {diff_c}°C")
print(f"In Fahrenheit: {diff_f}°F")
print(f"In Kelvin: {diff_k}K")

# Weather examples
print("\nWeather examples:")
temperatures_c = [-10, 0, 10, 20, 30, 40]
print("Celsius | Fahrenheit | Kelvin")
print("-" * 30)
for temp_c in temperatures_c:
    temp_f = celsius_to_fahrenheit(temp_c)
    temp_k = celsius_to_kelvin(temp_c)
    print("6.1f")
