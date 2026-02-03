# Archivo: 44_06_anagramas_permutaciones.py
# Descripción: Anagramas y permutaciones de strings

print("=== 6. Anagramas y Permutaciones ===\n")


def son_anagramas(str1, str2):
    """Verifica si dos strings son anagramas."""
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


def contar_anagramas(lista_palabras):
    """Agrupa palabras que son anagramas."""
    grupos = {}
    for palabra in lista_palabras:
        clave = ''.join(sorted(palabra))
        if clave not in grupos:
            grupos[clave] = []
        grupos[clave].append(palabra)
    return grupos


def encontrar_permutaciones(s):
    """Encuentra todas las permutaciones de un string."""
    if len(s) <= 1:
        return [s]

    permutaciones = []
    for i, char in enumerate(s):
        resto = s[:i] + s[i + 1:]
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
