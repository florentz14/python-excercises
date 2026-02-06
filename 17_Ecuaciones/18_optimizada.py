# Archivo: 31_02_optimizada.py
# Descripción: Integración optimizada con detalles y error

from integracion_util import f_original, integrar_funcion


if __name__ == "__main__":
    print("=== Versión 2: Optimizada y Mejorada ===\n")
    print("Integración optimizada:")
    resultado, error = integrar_funcion(f_original, -4, -3)
