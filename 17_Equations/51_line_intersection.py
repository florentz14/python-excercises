# Archivo: 50_04_interseccion_lineas.py
# Descripción: Intersección de líneas y segmentos

print("=== 4. Intersección de Líneas ===\n")


def interseccion_lineas(p1, p2, p3, p4):
    """
    Punto de intersección de dos líneas (p1-p2 y p3-p4).
    Retorna (x, y) o None si son paralelas.
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(denom) < 1e-10:
        return None
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
    x = x1 + t * (x2 - x1)
    y = y1 + t * (y2 - y1)
    return (x, y)


def interseccion_segmentos(p1, p2, p3, p4):
    """Indica si los segmentos (p1-p2) y (p3-p4) se intersecan."""

    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

    return ccw(p1, p3, p4) != ccw(p2, p3, p4) and ccw(p1, p2, p3) != ccw(p1, p2, p4)


if __name__ == "__main__":
    linea1_p1 = (0, 0)
    linea1_p2 = (2, 2)
    linea2_p1 = (0, 2)
    linea2_p2 = (2, 0)
    interseccion = interseccion_lineas(linea1_p1, linea1_p2, linea2_p1, linea2_p2)
    print(f"Línea 1: {linea1_p1} a {linea1_p2}")
    print(f"Línea 2: {linea2_p1} a {linea2_p2}")
    print(f"Intersección: {interseccion}")
    se_intersecan = interseccion_segmentos(linea1_p1, linea1_p2, linea2_p1, linea2_p2)
    print(f"¿Segmentos se intersecan? {se_intersecan}")
