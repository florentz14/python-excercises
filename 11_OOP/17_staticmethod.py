# -------------------------------------------------
# File: 17_staticmethod.py
# Description: @staticmethod decorator.
#              Utility methods that don't need class or instance.
# -------------------------------------------------


class MathUtils:
    """Utility class with static methods."""

    @staticmethod
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def factorial(n):
        """Calculate factorial."""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    @staticmethod
    def gcd(a, b):
        """Calculate greatest common divisor."""
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        """Calculate least common multiple."""
        return abs(a * b) // MathUtils.gcd(a, b)


class StringUtils:
    """String utility functions."""

    @staticmethod
    def is_palindrome(text):
        """Check if string is palindrome."""
        cleaned = ''.join(c.lower() for c in text if c.isalnum())
        return cleaned == cleaned[::-1]

    @staticmethod
    def word_count(text):
        """Count words in text."""
        return len(text.split())

    @staticmethod
    def capitalize_words(text):
        """Capitalize first letter of each word."""
        return ' '.join(word.capitalize() for word in text.split())


class FileUtils:
    """File utility functions."""

    @staticmethod
    def get_file_extension(filename):
        """Get file extension."""
        return filename.split('.')[-1] if '.' in filename else ''

    @staticmethod
    def is_image_file(filename):
        """Check if file is an image."""
        image_extensions = {'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'}
        return FileUtils.get_file_extension(filename).lower() in image_extensions

    @staticmethod
    def format_file_size(bytes_size):
        """Format file size in human readable format."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes_size < 1024:
                return f"{bytes_size:.1f}{unit}"
            bytes_size /= 1024
        return f"{bytes_size:.1f}TB"


class TemperatureConverter:
    """Temperature conversion utilities."""

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Convert Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(celsius):
        """Convert Celsius to Kelvin."""
        return celsius + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        """Convert Kelvin to Celsius."""
        return kelvin - 273.15


# Demonstration
if __name__ == "__main__":
    print("=== @staticmethod Demo ===\n")

    # Math utilities
    print("Math utilities:")
    print(f"is_prime(17): {MathUtils.is_prime(17)}")
    print(f"is_prime(18): {MathUtils.is_prime(18)}")
    print(f"factorial(5): {MathUtils.factorial(5)}")
    print(f"gcd(48, 18): {MathUtils.gcd(48, 18)}")
    print(f"lcm(4, 5): {MathUtils.lcm(4, 5)}")

    # String utilities
    print("\nString utilities:")
    test_strings = ["racecar", "hello world", "A man a plan a canal Panama"]
    for s in test_strings:
        print(f"is_palindrome('{s}'): {StringUtils.is_palindrome(s)}")

    text = "hello world from python"
    print(f"word_count('{text}'): {StringUtils.word_count(text)}")
    print(f"capitalize_words('{text}'): {StringUtils.capitalize_words(text)}")

    # File utilities
    print("\nFile utilities:")
    files = ["document.pdf", "image.jpg", "script.py", "data.txt"]
    for filename in files:
        ext = FileUtils.get_file_extension(filename)
        is_image = FileUtils.is_image_file(filename)
        print(f"'{filename}': ext='{ext}', is_image={is_image}")

    sizes = [512, 1536, 1048576, 2147483648]
    for size in sizes:
        print(f"{size} bytes = {FileUtils.format_file_size(size)}")

    # Temperature conversion
    print("\nTemperature conversion:")
    celsius = 25
    fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
    kelvin = TemperatureConverter.celsius_to_kelvin(celsius)

    print(f"{celsius}°C = {fahrenheit}°F = {kelvin}K")

    # Reverse conversions
    back_to_c = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {back_to_c}°C")

    print("\n=== Static Method Characteristics ===")
    print("- No 'self' or 'cls' parameter")
    print("- Cannot access instance or class attributes")
    print("- Can be called on class or instance")
    print("- Utility functions related to the class")
    print("- Don't depend on object state")

    print("\n=== When to Use Static Methods ===")
    print("- Utility functions")
    print("- Helper functions")
    print("- Pure functions (same input = same output)")
    print("- Functions that don't need object state")
    print("- Grouping related functions in a namespace")

    print("\n=== Class Method vs Static Method ===")
    print("Class method: operates on class, has 'cls' parameter")
    print("Static method: utility function, no 'self' or 'cls'")
    print("Both can be called on class or instance")