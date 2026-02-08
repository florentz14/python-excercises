# -------------------------------------------------
# File Name: 09_z_algorithm.py
# Author: Florentino Báez
# Date: Data Structures - String Algorithms
# Description: Z-Algorithm for pattern search in text.
#              Builds the Z-array where Z[i] indicates the length
#              of the longest prefix of the string that matches the
#              substring starting at position i. To search, concatenates
#              pattern + "$" + text and looks for Z[i] == m.
#              Complexity: O(n + m) in time and space.
# -------------------------------------------------

print("=== 2. Algoritmo Z-Algorithm ===\n")


def construir_z_array(cadena):
    """
    Builds the Z array.
    Z[i] = length of the longest prefix starting at i that is a prefix of the string.
    Complexity: O(n)
    """
    n = len(cadena)
    z = [0] * n
    z[0] = n         # Z[0] = total length by definition
    l, r = 0, 0      # Window [l, r] of the rightmost Z-box

    for i in range(1, n):
        if i <= r:
            # Reuse information from the previous Z-box
            z[i] = min(r - i + 1, z[i - l])

        # Extend the match character by character
        while i + z[i] < n and cadena[z[i]] == cadena[i + z[i]]:
            z[i] += 1

        # Update the Z-box if the match extends beyond r
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z


def z_algorithm_busqueda(texto, patron):
    """
    Searches for the pattern in the text using Z-algorithm.
    Complexity: O(n + m)
    """
    m = len(patron)
    if m == 0:
        return [0]

    # Concatenate pattern + separator + text
    combinado = patron + "$" + texto
    z = construir_z_array(combinado)

    ocurrencias = []
    for i in range(m + 1, len(combinado)):
        if z[i] == m:  # Z[i] == pattern length = full match
            ocurrencias.append(i - m - 1)  # Convert index to position in text

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
