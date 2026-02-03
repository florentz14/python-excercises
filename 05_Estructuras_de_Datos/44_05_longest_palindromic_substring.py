# Archivo: 44_05_longest_palindromic_substring.py
# Descripción: Subcadena palindrómica más larga

print("=== 5. Subcadena Palindrómica Más Larga ===\n")


def longest_palindromic_substring(s):
    """
    Subcadena palindrómica más larga (expansión desde centro).
    Complejidad: O(n²)
    """
    if not s:
        return ""

    def expandir_desde_centro(izquierda, derecha):
        while izquierda >= 0 and derecha < len(s) and s[izquierda] == s[derecha]:
            izquierda -= 1
            derecha += 1
        return s[izquierda + 1:derecha]

    subcadena_max = ""

    for i in range(len(s)):
        pal1 = expandir_desde_centro(i, i)
        pal2 = expandir_desde_centro(i, i + 1)
        if len(pal1) > len(subcadena_max):
            subcadena_max = pal1
        if len(pal2) > len(subcadena_max):
            subcadena_max = pal2

    return subcadena_max


if __name__ == "__main__":
    cadena_pal = "babad"
    print(f"Cadena: '{cadena_pal}'")
    palindromo_max = longest_palindromic_substring(cadena_pal)
    print(f"Subcadena palindrómica más larga: '{palindromo_max}'")
