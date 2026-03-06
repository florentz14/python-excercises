# ---------------------------------------------------------------------------
# 185. Convert Decimal to Binary List (list of digits 0/1)
# ---------------------------------------------------------------------------
# Descripción: Convert Decimal to Binary List (list of digits 0/1)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def decimal_to_binary_list(n: int) -> list[int]:
    if n == 0:
        return [0]
    bits = []
    while n > 0:
        bits.append(n % 2)
        n //= 2
    return bits[::-1]


print(decimal_to_binary_list(8))   # [1, 0, 0, 0]
print(decimal_to_binary_list(45))  # [1, 0, 1, 1, 0, 1]
print(decimal_to_binary_list(100)) # [1, 1, 0, 0, 1, 0, 0]
