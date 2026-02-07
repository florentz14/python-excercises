# ---------------------------------------------------------------------------
# Lista Simple - 21: Metodo count()
# ---------------------------------------------------------------------------
# Descripcion: El metodo count() retorna el numero de veces que un valor
#              aparece en la lista. Si el valor no existe, retorna 0.
# Sintaxis:    lista.count(valor)
# Complejidad: O(n) - recorre toda la lista
# ---------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "banana", "grape", "banana", "mango"]

# Contar ocurrencias de "banana"
count = fruits.count("banana")
print(f"'banana' appears {count} times")
# Output: 'banana' appears 3 times

# Contar un elemento que no existe
count_pear = fruits.count("pear")
print(f"'pear' appears {count_pear} times")
# Output: 'pear' appears 0 times

# --- Con numeros ---
numeros = [1, 3, 7, 3, 8, 3, 2, 3, 9]
print(f"\nEl 3 aparece {numeros.count(3)} veces")
# Output: El 3 aparece 4 veces

# ---------------------------------------------------------------------------
# Uso practico: encontrar el elemento mas frecuente
# ---------------------------------------------------------------------------
votos = ["A", "B", "A", "C", "A", "B", "A", "C", "B"]

candidatos = set(votos)  # Eliminar duplicados para iterar
print("\nResultados de votacion:")
for candidato in sorted(candidatos):
    total = votos.count(candidato)
    print(f"  Candidato {candidato}: {total} votos")

# Encontrar el ganador
ganador = max(candidatos, key=votos.count)
print(f"Ganador: {ganador} con {votos.count(ganador)} votos")

# ---------------------------------------------------------------------------
# Uso practico: verificar si hay duplicados
# ---------------------------------------------------------------------------
lista = [1, 2, 3, 4, 5, 3]
hay_duplicados = any(lista.count(x) > 1 for x in lista)
print(f"\nHay duplicados en {lista}: {hay_duplicados}")
# Output: True
