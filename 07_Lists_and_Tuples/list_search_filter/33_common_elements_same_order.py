# ---------------------------------------------------------------------------
# 133. Check If Common Elements in Two Lists Appear in Same Order
# ---------------------------------------------------------------------------
# Descripción: Check If Common Elements in Two Lists Appear in Same Order
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def common_same_order(a: list, b: list) -> bool:
    common = [x for x in a if x in b]
    order_in_b = [b.index(x) for x in common if x in b]
    return order_in_b == sorted(order_in_b)


color1 = ['red', 'green', 'black', 'orange']
color2 = ['red', 'pink', 'green', 'white', 'black']
print(common_same_order(color1, color2))  # True
