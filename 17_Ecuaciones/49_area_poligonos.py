# Archivo: 50_02_area_poligonos.py
# Descripción: Área de polígonos (shoelace) y triángulos

print("=== 2. Área de Polígonos ===\n")


def area_poligono_simple(puntos):
    """
    Área de un polígono simple (fórmula del shoelace).
    Puntos en orden horario o antihorario.
    """
    n = len(puntos)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += puntos[i][0] * puntos[j][1]
        area -= puntos[j][0] * puntos[i][1]
    return abs(area) / 2.0


def area_triangulo(p1, p2, p3):
    """Área de un triángulo (fórmula del determinante)."""
    return abs((p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1])) / 2.0)


if __name__ == "__main__":
    triangulo = [(0, 0), (4, 0), (2, 3)]
    print(f"Triángulo: {triangulo}")
    print(f"Área: {area_triangulo(triangulo[0], triangulo[1], triangulo[2]):.2f}")

    poligono = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(f"\nPolígono (rectángulo): {poligono}")
    print(f"Área: {area_poligono_simple(poligono):.2f}")
