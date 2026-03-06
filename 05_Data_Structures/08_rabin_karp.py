# -------------------------------------------------
# File Name: 08_rabin_karp.py
# Author: Florentino Báez
# Date: Data Structures - String Algorithms
# Description: Rabin-Karp algorithm for pattern matching.
#              Uses rolling hash to compare the pattern against
#              substrings of the text efficiently. Computes the
#              hash of the sliding window in O(1) and only
#              compares character by character when hashes match.
#              Complexity: O(n + m) average, O(n * m) worst case.
# -------------------------------------------------

print("=== Algoritmos Avanzados de Strings ===\n")
print("=== 1. Algoritmo Rabin-Karp ===\n")


def rabin_karp(texto, patron, base=256, primo=101):
    """
    Pattern search using Rabin-Karp (rolling hash).
    Complexity: O(n + m) average, O(n * m) worst case
    """
    n = len(texto)
    m = len(patron)

    if m == 0:
        return [0]
    if m > n:
        return []

    hash_patron = 0      # Hash of the pattern to search for
    hash_ventana = 0     # Hash of the current window in the text
    h = 1                # Positional value of the most significant digit
    # Compute h = base^(m-1) % primo (to remove the first character)
    for i in range(m - 1):
        h = (h * base) % primo

    # Compute initial hash of the pattern and of the first window
    for i in range(m):
        hash_patron = (base * hash_patron + ord(patron[i])) % primo
        hash_ventana = (base * hash_ventana + ord(texto[i])) % primo

    ocurrencias = []

    for i in range(n - m + 1):
        if hash_patron == hash_ventana:
            # Hashes match → verify character by character
            if texto[i:i+m] == patron:
                ocurrencias.append(i)

        if i < n - m:
            # Rolling hash: remove first character and add the next one
            hash_ventana = (base * (hash_ventana - ord(texto[i]) * h) + ord(texto[i + m])) % primo
            if hash_ventana < 0:
                hash_ventana = hash_ventana + primo  # Correct negative hash

    return ocurrencias


if __name__ == "__main__":
    texto_rk = "GEEKS FOR GEEKS"
    patron_rk = "GEEK"

    print(f"Texto: '{texto_rk}'")
    print(f"Patrón: '{patron_rk}'")
    ocurrencias_rk = rabin_karp(texto_rk, patron_rk)
    print(f"Ocurrencias (Rabin-Karp): {ocurrencias_rk}")
