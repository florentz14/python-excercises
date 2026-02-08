# -------------------------------------------------
# File Name: 30_trie.py
# Author: Florentino Báez
# Date: Data Structures - Advanced Structures
# Description: Trie (Prefix Tree).
#              Tree structure where each node represents a
#              character. Allows inserting, searching and
#              autocompleting words efficiently. Each path from
#              root to a node marked as end represents a word.
#              Complexity: O(m) per operation, m = word length.
# -------------------------------------------------

print("=== Estructuras de Datos Avanzadas ===\n")
print("=== 1. Trie (Árbol de Prefijos) ===\n")


class NodoTrie:
    """Node for the Trie tree."""

    def __init__(self):
        self.hijos = {}
        self.es_fin_palabra = False
        self.conteo = 0


class Trie:
    """
    Trie for storing and searching strings.
    Complexity: O(m) per operation, m = word length.
    """

    def __init__(self):
        self.raiz = NodoTrie()

    def insertar(self, palabra):
        nodo_actual = self.raiz
        for caracter in palabra:
            if caracter not in nodo_actual.hijos:
                nodo_actual.hijos[caracter] = NodoTrie()
            nodo_actual = nodo_actual.hijos[caracter]
            nodo_actual.conteo += 1
        nodo_actual.es_fin_palabra = True

    def buscar(self, palabra):
        nodo_actual = self.raiz
        for caracter in palabra:
            if caracter not in nodo_actual.hijos:
                return False
            nodo_actual = nodo_actual.hijos[caracter]
        return nodo_actual.es_fin_palabra

    def buscar_prefijo(self, prefijo):
        nodo_actual = self.raiz
        for caracter in prefijo:
            if caracter not in nodo_actual.hijos:
                return False
            nodo_actual = nodo_actual.hijos[caracter]
        return True

    def autocompletar(self, prefijo):
        nodo_actual = self.raiz
        for caracter in prefijo:
            if caracter not in nodo_actual.hijos:
                return []
            nodo_actual = nodo_actual.hijos[caracter]
        palabras = []

        def dfs(nodo, prefijo_actual):
            if nodo.es_fin_palabra:
                palabras.append(prefijo_actual)
            for c, hijo in nodo.hijos.items():
                dfs(hijo, prefijo_actual + c)

        dfs(nodo_actual, prefijo)
        return palabras

    def eliminar(self, palabra):
        def _eliminar(nodo, pal, indice):
            if indice == len(pal):
                if not nodo.es_fin_palabra:
                    return False
                nodo.es_fin_palabra = False
                return len(nodo.hijos) == 0
            c = pal[indice]
            if c not in nodo.hijos:
                return False
            debe_eliminar = _eliminar(nodo.hijos[c], pal, indice + 1)
            if debe_eliminar:
                del nodo.hijos[c]
                nodo.conteo -= 1
                return len(nodo.hijos) == 0 and not nodo.es_fin_palabra
            return False

        _eliminar(self.raiz, palabra, 0)


if __name__ == "__main__":
    trie = Trie()
    palabras = ["apple", "app", "apricot", "banana", "band", "bandana"]

    print("Insertando palabras:", palabras)
    for palabra in palabras:
        trie.insertar(palabra)

    print(f"\n¿'apple' existe? {trie.buscar('apple')}")
    print(f"¿'apples' existe? {trie.buscar('apples')}")
    print(f"¿Existe prefijo 'app'? {trie.buscar_prefijo('app')}")
    print(f"Autocompletar 'ban': {trie.autocompletar('ban')}")
