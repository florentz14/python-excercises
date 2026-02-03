# Archivo: 50_06_punto_en_poligono.py
# Descripción: Punto en polígono (ray casting)

print("=== 6. Punto en Polígono (Ray Casting) ===\n")


def punto_en_poligono(punto, poligono):
    """True si el punto está dentro del polígono (ray casting). O(n)."""
    x, y = punto
    n = len(poligono)
    dentro = False
    j = n - 1
    for i in range(n):
        xi, yi = poligono[i]
        xj, yj = poligono[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            dentro = not dentro
        j = i
    return dentro


if __name__ == "__main__":
    poligono_test = [(0, 0), (4, 0), (4, 4), (0, 4)]
    punto_dentro = (2, 2)
    punto_fuera = (5, 5)
    print(f"Polígono: {poligono_test}")
    print(f"¿Punto {punto_dentro} está dentro? {punto_en_poligono(punto_dentro, poligono_test)}")
    print(f"¿Punto {punto_fuera} está dentro? {punto_en_poligono(punto_fuera, poligono_test)}")
