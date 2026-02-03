# Archivo: 45_07_conversion_bases.py
# Descripción: Conversión entre bases numéricas

print("=== 7. Conversión de Bases Numéricas ===\n")


def convertir_base(n, base_destino, base_origen=10):
    """
    Convierte un número de base_origen a base_destino.
    """
    if base_origen != 10:
        n_decimal = 0
        n_str = str(n)
        for i, digito in enumerate(reversed(n_str)):
            n_decimal += int(digito) * (base_origen ** i)
        n = n_decimal

    if base_destino == 10:
        return str(n)

    resultado = []
    n_actual = n

    while n_actual > 0:
        resto = n_actual % base_destino
        if resto < 10:
            resultado.append(str(resto))
        else:
            resultado.append(chr(ord('A') + resto - 10))
        n_actual //= base_destino

    return ''.join(reversed(resultado))


if __name__ == "__main__":
    numero_conv = 255
    print(f"Número en decimal: {numero_conv}")
    print(f"Binario: {convertir_base(numero_conv, 2)}")
    print(f"Octal: {convertir_base(numero_conv, 8)}")
    print(f"Hexadecimal: {convertir_base(numero_conv, 16)}")
