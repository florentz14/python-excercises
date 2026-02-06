# Archivo: 25_06_sistemas_ejemplos.py
# Descripción: Sistemas del código original y comentado

from datos_sistema import A_original, b_original, B_comentado, d_comentado
from resolver_mejorado import resolver_sistema_mejorado


if __name__ == "__main__":
    print("=== Versión 6: Sistema del Código Original ===\n")

    print("Sistema original (A, b):")
    x1, info1 = resolver_sistema_mejorado(A_original, b_original, mostrar_proceso=True)

    print("\nSistema comentado (B, d):")
    x2, info2 = resolver_sistema_mejorado(B_comentado, d_comentado, mostrar_proceso=True)
