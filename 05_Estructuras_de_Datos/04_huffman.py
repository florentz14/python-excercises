# Archivo: 42_04_huffman.py
# Descripción: Codificación de Huffman (greedy)

import heapq

print("=== 4. Codificación de Huffman ===\n")


class NodoHuffman:
    """Nodo para el árbol de Huffman."""

    def __init__(self, caracter=None, frecuencia=0, izquierda=None, derecha=None):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = izquierda
        self.derecha = derecha

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

    def es_hoja(self):
        return self.izquierda is None and self.derecha is None


def construir_arbol_huffman(frecuencias):
    """
    Construye el árbol de Huffman (greedy).
    Estrategia: Combinar siempre los dos nodos con menor frecuencia.
    Complejidad: O(n log n)
    """
    cola = []
    for caracter, frecuencia in frecuencias.items():
        heapq.heappush(cola, NodoHuffman(caracter, frecuencia))

    while len(cola) > 1:
        izquierda = heapq.heappop(cola)
        derecha = heapq.heappop(cola)
        nodo_fusion = NodoHuffman(
            frecuencia=izquierda.frecuencia + derecha.frecuencia,
            izquierda=izquierda,
            derecha=derecha
        )
        heapq.heappush(cola, nodo_fusion)

    return cola[0] if cola else None


def generar_codigos_huffman(nodo, codigo="", codigos=None):
    """Genera los códigos binarios recorriendo el árbol."""
    if codigos is None:
        codigos = {}
    if nodo is None:
        return codigos
    if nodo.es_hoja():
        codigos[nodo.caracter] = codigo if codigo else "0"
        return codigos
    generar_codigos_huffman(nodo.izquierda, codigo + "0", codigos)
    generar_codigos_huffman(nodo.derecha, codigo + "1", codigos)
    return codigos


def codificar_huffman(texto):
    """Codifica un texto usando Huffman."""
    frecuencias = {}
    for caracter in texto:
        frecuencias[caracter] = frecuencias.get(caracter, 0) + 1

    raiz = construir_arbol_huffman(frecuencias)
    if raiz is None:
        return {}, ""

    codigos = generar_codigos_huffman(raiz)
    texto_codificado = ''.join(codigos[caracter] for caracter in texto)
    return codigos, texto_codificado


if __name__ == "__main__":
    texto_huffman = "hello world"
    print(f"Texto original: '{texto_huffman}'")

    codigos, texto_cod = codificar_huffman(texto_huffman)
    print("\nCódigos de Huffman:")
    for caracter, codigo in sorted(codigos.items()):
        print(f"  '{caracter}': {codigo}")

    print(f"\nTexto codificado: {texto_cod}")
    print(f"Longitud original: {len(texto_huffman) * 8} bits (ASCII)")
    print(f"Longitud codificada: {len(texto_cod)} bits")
    print(f"Compresión: {len(texto_cod) / (len(texto_huffman) * 8) * 100:.1f}%")
