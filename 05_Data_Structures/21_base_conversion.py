# -------------------------------------------------
# File Name: 21_base_conversion.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Base conversion. Converts numbers between different numeral bases.
# -------------------------------------------------

def convert_base(n, target_base, source_base=10):
    """
    Converts a number from source_base to target_base.
    Returns string representation in target base.
    """
    # Step 1: Convert from source base to decimal (if not base 10)
    if source_base != 10:
        n_decimal = 0
        n_str = str(n)
        for i, digit in enumerate(reversed(n_str)):
            n_decimal += int(digit) * (source_base ** i)
        n = n_decimal

    if target_base == 10:
        return str(n)

    # Step 2: Convert from decimal to target base (successive divisions)
    result = []
    current = n

    while current > 0:
        remainder = current % target_base
        if remainder < 10:
            result.append(str(remainder))
        else:
            result.append(chr(ord('A') + remainder - 10))
        current //= target_base

    return ''.join(reversed(result))


if __name__ == "__main__":
    print("=== Mathematical Algorithms: Base Conversion ===\n")

    num = 255
    print(f"Decimal: {num}")
    print(f"Binary: {convert_base(num, 2)}")
    print(f"Octal: {convert_base(num, 8)}")
    print(f"Hexadecimal: {convert_base(num, 16)}")
