# -------------------------------------------------
# File Name: 13_anagramas_permutaciones.py
# Author: Florentino Báez
# Date: Data Structures - String Algorithms
# Description: Anagrams and String Permutations.
#              Checks if two words are anagrams (same letters
#              in different order), groups anagrams from a list,
#              and generates all permutations of a string
#              using recursion. Permutation complexity: O(n!).
# -------------------------------------------------

print("=== 6. Anagramas y Permutaciones ===\n")


def son_anagramas(str1, str2):
    """Checks if two strings are anagrams."""
    if len(str1) != len(str2):
        return False  # Different length → cannot be anagrams
    # If sorting both yields the same letters, they are anagrams
    return sorted(str1) == sorted(str2)


def contar_anagramas(lista_palabras):
    """Groups words that are anagrams."""
    grupos = {}
    for palabra in lista_palabras:
        # Key: sorted letters (anagrams share the same key)
        clave = ''.join(sorted(palabra))
        if clave not in grupos:
            grupos[clave] = []
        grupos[clave].append(palabra)
    return grupos


def encontrar_permutaciones(s):
    """Finds all permutations of a string using recursion."""
    if len(s) <= 1:
        return [s]  # Base case: single character has only one permutation

    permutaciones = []
    for i, char in enumerate(s):
        resto = s[:i] + s[i + 1:]  # Remove the current character
        # Recursion: generate permutations of the rest and prepend char
        for perm in encontrar_permutaciones(resto):
            permutaciones.append(char + perm)

    return permutaciones


if __name__ == "__main__":
    palabra1_anag = "listen"
    palabra2_anag = "silent"
    print(f"'{palabra1_anag}' y '{palabra2_anag}' son anagramas: {son_anagramas(palabra1_anag, palabra2_anag)}")

    lista_anagramas = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"\nLista: {lista_anagramas}")
    grupos = contar_anagramas(lista_anagramas)
    print("Grupos de anagramas:")
    for grupo in grupos.values():
        print(f"  {grupo}")

    cadena_perm = "abc"
    print(f"\nPermutaciones de '{cadena_perm}':")
    permutaciones = encontrar_permutaciones(cadena_perm)
    print(f"  {permutaciones}")
