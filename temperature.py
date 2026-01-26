# Temperature Conversion Program
# This program converts temperatures between Celsius, Fahrenheit, and Kelvin

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return fahrenheit_to_celsius(fahrenheit) + 273.15


def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))


# Test the conversion functions
print("Temperature Conversion Examples")
print("=" * 40)

# Example 1: Convert 25°C to Fahrenheit and Kelvin
celsius_temp = 25
print(f"\n{celsius_temp}°C conversions:")
print(f"  To Fahrenheit: {celsius_to_fahrenheit(celsius_temp):.2f}°F")
print(f"  To Kelvin: {celsius_to_kelvin(celsius_temp):.2f}K")

# Example 2: Convert 98.6°F to Celsius and Kelvin
fahrenheit_temp = 98.6
print(f"\n{fahrenheit_temp}°F conversions:")
print(f"  To Celsius: {fahrenheit_to_celsius(fahrenheit_temp):.2f}°C")
print(f"  To Kelvin: {fahrenheit_to_kelvin(fahrenheit_temp):.2f}K")

# Example 3: Convert 273.15K to Celsius and Fahrenheit
kelvin_temp = 273.15
print(f"\n{kelvin_temp}K conversions:")
print(f"  To Celsius: {kelvin_to_celsius(kelvin_temp):.2f}°C")
print(f"  To Fahrenheit: {kelvin_to_fahrenheit(kelvin_temp):.2f}°F")
