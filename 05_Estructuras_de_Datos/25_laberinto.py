# -------------------------------------------------
# File Name: 25_laberinto.py
# Author: Florentino Báez
# Date: Estructuras de Datos - Backtracking
# Description: Resolución de Laberintos (Backtracking).
#              Encuentra un camino desde el inicio hasta el destino
#              en una matriz donde 0 = camino libre y 1 = pared.
#              Explora las 4 direcciones (derecha, abajo, izquierda,
#              arriba) y retrocede si llega a un callejón sin salida.
# -------------------------------------------------

print("=== 3. Resolución de Laberintos ===\n")


def resolver_laberinto(laberinto, inicio, destino):
    """
    Resuelve un laberinto usando backtracking.
    0 = camino libre, 1 = pared.
    Retorna el camino si existe, None si no.
    """
    n, m = len(laberinto), len(laberinto[0])
    visitados = [[False] * m for _ in range(n)]
    camino = []

    direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def es_valido(x, y):
        return (0 <= x < n and 0 <= y < m and
                laberinto[x][y] == 0 and not visitados[x][y])

    def backtrack(x, y):
        if (x, y) == destino:
            camino.append((x, y))
            return True
        visitados[x][y] = True
        camino.append((x, y))
        for dx, dy in direcciones:
            nuevo_x, nuevo_y = x + dx, y + dy
            if es_valido(nuevo_x, nuevo_y):
                if backtrack(nuevo_x, nuevo_y):
                    return True
        camino.pop()
        return False

    if backtrack(inicio[0], inicio[1]):
        return camino
    return None


def imprimir_laberinto_con_camino(laberinto, camino):
    """Imprime el laberinto marcando el camino."""
    n, m = len(laberinto), len(laberinto[0])
    solucion = [[' ' if laberinto[i][j] == 0 else '#' for j in range(m)] for i in range(n)]
    for x, y in camino:
        solucion[x][y] = '*'
    if camino:
        solucion[camino[0][0]][camino[0][1]] = 'S'
        solucion[camino[-1][0]][camino[-1][1]] = 'E'
    print("  " + "".join(str(i % 10) for i in range(m)))
    for i, fila in enumerate(solucion):
        print(f"{i % 10} " + "".join(fila))


if __name__ == "__main__":
    laberinto = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    inicio = (0, 0)
    destino = (4, 4)

    print("Laberinto (0=camino, 1=pared):")
    for fila in laberinto:
        print(f"  {fila}")

    camino = resolver_laberinto(laberinto, inicio, destino)
    if camino:
        print(f"\nCamino encontrado ({len(camino)} pasos):")
        imprimir_laberinto_con_camino(laberinto, camino)
    else:
        print("\nNo se encontró camino")
