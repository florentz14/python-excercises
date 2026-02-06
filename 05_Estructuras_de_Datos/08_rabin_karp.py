# Archivo: 44_01_rabin_karp.py
# Descripción: Algoritmo Rabin-Karp (búsqueda de patrón con rolling hash)

print("=== Algoritmos Avanzados de Strings ===\n")
print("=== 1. Algoritmo Rabin-Karp ===\n")


def rabin_karp(texto, patron, base=256, primo=101):
    """
    Búsqueda de patrón usando Rabin-Karp (rolling hash).
    Complejidad: O(n + m) promedio, O(n * m) peor caso
    """
    n = len(texto)
    m = len(patron)

    if m == 0:
        return [0]
    if m > n:
        return []

    hash_patron = 0
    hash_ventana = 0
    h = 1
    for i in range(m - 1):
        h = (h * base) % primo

    for i in range(m):
        hash_patron = (base * hash_patron + ord(patron[i])) % primo
        hash_ventana = (base * hash_ventana + ord(texto[i])) % primo

    ocurrencias = []

    for i in range(n - m + 1):
        if hash_patron == hash_ventana:
            if texto[i:i+m] == patron:
                ocurrencias.append(i)

        if i < n - m:
            hash_ventana = (base * (hash_ventana - ord(texto[i]) * h) + ord(texto[i + m])) % primo
            if hash_ventana < 0:
                hash_ventana = hash_ventana + primo

    return ocurrencias


if __name__ == "__main__":
    texto_rk = "GEEKS FOR GEEKS"
    patron_rk = "GEEK"

    print(f"Texto: '{texto_rk}'")
    print(f"Patrón: '{patron_rk}'")
    ocurrencias_rk = rabin_karp(texto_rk, patron_rk)
    print(f"Ocurrencias (Rabin-Karp): {ocurrencias_rk}")
