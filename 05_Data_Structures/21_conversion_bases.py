# -------------------------------------------------
# File Name: 21_conversion_bases.py
# Author: Florentino Báez
# Date: Data Structures - Mathematical Algorithms
# Description: Conversion between Numeric Bases.
#              Converts numbers between different bases (binary,
#              octal, decimal, hexadecimal, etc.). First converts
#              to decimal (if not already) and then to the target
#              base by successive divisions and remainders.
# -------------------------------------------------

print("=== 7. Conversión de Bases Numéricas ===\n")


def convertir_base(n, base_destino, base_origen=10):
    """
    Converts a number from base_origen to base_destino.
    """
    # Step 1: Convert from base_origen to decimal (if not base 10)
    if base_origen != 10:
        n_decimal = 0
        n_str = str(n)
        for i, digito in enumerate(reversed(n_str)):
            n_decimal += int(digito) * (base_origen ** i)  # Add digit × base^position
        n = n_decimal

    if base_destino == 10:
        return str(n)  # Already in decimal

    # Step 2: Convert from decimal to base_destino (successive divisions)
    resultado = []
    n_actual = n

    while n_actual > 0:
        resto = n_actual % base_destino  # Get the least significant digit
        if resto < 10:
            resultado.append(str(resto))
        else:
            # For bases > 10, use letters (A=10, B=11, ..., F=15)
            resultado.append(chr(ord('A') + resto - 10))
        n_actual //= base_destino

    return ''.join(reversed(resultado))  # Reverse for correct order


if __name__ == "__main__":
    numero_conv = 255
    print(f"Número en decimal: {numero_conv}")
    print(f"Binario: {convertir_base(numero_conv, 2)}")
    print(f"Octal: {convertir_base(numero_conv, 8)}")
    print(f"Hexadecimal: {convertir_base(numero_conv, 16)}")
