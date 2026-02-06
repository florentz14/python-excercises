# Archivo: 45_02_euclides.py
# Descripción: Algoritmo de Euclides (MCD, MCM, extendido)

print("=== 2. Algoritmo de Euclides (MCD) ===\n")


def euclides_mcd(a, b):
    """
    Máximo Común Divisor (algoritmo de Euclides).
    Complejidad: O(log min(a, b))
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)


def euclides_mcd_recursivo(a, b):
    """Versión recursiva del algoritmo de Euclides."""
    if b == 0:
        return abs(a)
    return euclides_mcd_recursivo(b, a % b)


def euclides_mcm(a, b):
    """Mínimo Común Múltiplo: MCM(a, b) = |a * b| / MCD(a, b)."""
    mcd = euclides_mcd(a, b)
    return abs(a * b) // mcd if mcd != 0 else 0


def euclides_extendido(a, b):
    """
    Euclides extendido: encuentra x, y tal que a*x + b*y = MCD(a, b).
    Retorna: (mcd, x, y)
    """
    if a == 0:
        return abs(b), 0, 1 if b >= 0 else -1

    mcd, x1, y1 = euclides_extendido(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return mcd, x, y


if __name__ == "__main__":
    a_euclides = 48
    b_euclides = 18

    print(f"a = {a_euclides}, b = {b_euclides}")
    print(f"MCD (iterativo): {euclides_mcd(a_euclides, b_euclides)}")
    print(f"MCD (recursivo): {euclides_mcd_recursivo(a_euclides, b_euclides)}")
    print(f"MCM: {euclides_mcm(a_euclides, b_euclides)}")

    mcd_ext, x, y = euclides_extendido(a_euclides, b_euclides)
    print(f"Euclides extendido: {mcd_ext} = {a_euclides}*{x} + {b_euclides}*{y}")
