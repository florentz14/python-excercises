# Archivo: 44_02_z_algorithm.py
# Descripción: Z-Algorithm (Z-array y búsqueda de patrón)

print("=== 2. Algoritmo Z-Algorithm ===\n")


def construir_z_array(cadena):
    """
    Construye el array Z.
    Z[i] = longitud del prefijo más largo que empieza en i y es prefijo de la cadena.
    Complejidad: O(n)
    """
    n = len(cadena)
    z = [0] * n
    z[0] = n
    l, r = 0, 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        while i + z[i] < n and cadena[z[i]] == cadena[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z


def z_algorithm_busqueda(texto, patron):
    """
    Busca el patrón en el texto usando Z-algorithm.
    Complejidad: O(n + m)
    """
    m = len(patron)
    if m == 0:
        return [0]

    combinado = patron + "$" + texto
    z = construir_z_array(combinado)

    ocurrencias = []
    for i in range(m + 1, len(combinado)):
        if z[i] == m:
            ocurrencias.append(i - m - 1)

    return ocurrencias


if __name__ == "__main__":
    texto_z = "ABABDABACDABABCABCABAB"
    patron_z = "ABABCABAB"

    print(f"Texto: '{texto_z}'")
    print(f"Patrón: '{patron_z}'")
    ocurrencias_z = z_algorithm_busqueda(texto_z, patron_z)
    print(f"Ocurrencias (Z-Algorithm): {ocurrencias_z}")

    cadena_z = "aabxaabxcaabxaabxay"
    z_array = construir_z_array(cadena_z)
    print(f"\nCadena: '{cadena_z}'")
    print(f"Z-array: {z_array}")
