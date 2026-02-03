# Archivo: resolver_mejorado.py
# Descripción: Resolver sistema de ecuaciones lineales (versión mejorada)

import numpy as np


def resolver_sistema_mejorado(A, b, mostrar_proceso=True, tolerancia=1e-10):
    """
    Resuelve un sistema de ecuaciones lineales Ax = b de manera mejorada.

    Parámetros:
    - A: Matriz de coeficientes (numpy array)
    - b: Vector de términos independientes (numpy array)
    - mostrar_proceso: Si mostrar el proceso paso a paso
    - tolerancia: Tolerancia para considerar si el determinante es cero

    Retorna:
    - x: Vector solución, o None si no hay solución única
    - info: Diccionario con información sobre la solución
    """
    try:
        if A.shape[0] != A.shape[1]:
            raise ValueError("La matriz A debe ser cuadrada")

        if A.shape[0] != b.shape[0]:
            raise ValueError("Las dimensiones de A y b no coinciden")

        determinante = np.linalg.det(A)

        if mostrar_proceso:
            print(f'Determinante: {determinante:.6f}')

        if abs(determinante) < tolerancia:
            if mostrar_proceso:
                print('[AVISO] La matriz es singular (determinante ~ 0)')
                print('   El sistema puede tener infinitas soluciones o ninguna solución')
            return None, {'singular': True, 'determinante': determinante}

        x = np.linalg.solve(A, b)
        b_verificacion = np.dot(A, x)
        error = np.linalg.norm(b - b_verificacion)

        info = {
            'singular': False,
            'determinante': determinante,
            'solucion': x,
            'error': error,
            'verificacion_correcta': error < tolerancia
        }

        if mostrar_proceso:
            print(f'\n[OK] Solución del sistema:')
            print(x)
            print(f'\n[OK] Verificación: A * x = b')
            print(f'   Calculado: {b_verificacion}')
            print(f'   Esperado:  {b}')
            print(f'   Error: {error:.2e}')
            if error < tolerancia:
                print('   La solución es correcta')
            else:
                print('   [AVISO] Hay un error significativo en la verificación')

        return x, info

    except np.linalg.LinAlgError as e:
        if mostrar_proceso:
            print(f'[ERROR] Error en álgebra lineal: {e}')
        return None, {'error': str(e)}
    except Exception as e:
        if mostrar_proceso:
            print(f'[ERROR] Error: {e}')
        return None, {'error': str(e)}
