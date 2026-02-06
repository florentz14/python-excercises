# Archivo: 50_01_distancias.py
# Descripción: Distancias entre puntos (Euclidiana, Manhattan, Chebyshev)

import math

print("=== Geometría Computacional ===\n")
print("=== 1. Distancias entre Puntos ===\n")


class Punto:
    """Punto en 2D."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

    def distancia_euclidiana(self, otro):
        return math.sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2)

    def distancia_manhattan(self, otro):
        return abs(self.x - otro.x) + abs(self.y - otro.y)

    def distancia_chebyshev(self, otro):
        return max(abs(self.x - otro.x), abs(self.y - otro.y))


def distancia_puntos(p1, p2):
    """Distancia euclidiana entre dos puntos (tuplas)."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


if __name__ == "__main__":
    p1 = Punto(0, 0)
    p2 = Punto(3, 4)
    print(f"Punto 1: {p1}")
    print(f"Punto 2: {p2}")
    print(f"Distancia euclidiana: {p1.distancia_euclidiana(p2):.2f}")
    print(f"Distancia Manhattan: {p1.distancia_manhattan(p2)}")
    print(f"Distancia Chebyshev: {p1.distancia_chebyshev(p2)}")
