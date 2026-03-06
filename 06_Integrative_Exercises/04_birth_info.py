"""
Ejercicio: Información Personal por Fecha de Nacimiento

Programa que calcula información sobre una persona basada en su nombre y fecha de nacimiento.
"""

from datetime import datetime, date


def calcular_edad(fecha_nacimiento):
    """
    Calcula la edad actual de una persona.

    Args:
        fecha_nacimiento (date): La fecha de nacimiento

    Returns:
        int: La edad en años
    """
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    return edad


def dias_hasta_cumpleaños(fecha_nacimiento):
    """
    Calcula los días que faltan para el próximo cumpleaños.

    Args:
        fecha_nacimiento (date): La fecha de nacimiento

    Returns:
        int: Días hasta el próximo cumpleaños
    """
    hoy = date.today()
    proximo_cumple = date(
        hoy.year, fecha_nacimiento.month, fecha_nacimiento.day)

    if proximo_cumple < hoy:
        proximo_cumple = date(
            hoy.year + 1, fecha_nacimiento.month, fecha_nacimiento.day)

    dias_faltantes = (proximo_cumple - hoy).days
    return dias_faltantes


def obtener_signo_zodiaco_occidental(fecha_nacimiento):
    """
    Determina el signo del zodíaco occidental.

    Args:
        fecha_nacimiento (date): La fecha de nacimiento

    Returns:
        str: El signo del zodíaco occidental
    """
    mes = fecha_nacimiento.month
    dia = fecha_nacimiento.day

    signos = {
        "Aries": (3, 21, 4, 19),
        "Tauro": (4, 20, 5, 20),
        "Géminis": (5, 21, 6, 20),
        "Cáncer": (6, 21, 7, 22),
        "Leo": (7, 23, 8, 22),
        "Virgo": (8, 23, 9, 22),
        "Libra": (9, 23, 10, 22),
        "Escorpio": (10, 23, 11, 21),
        "Sagitario": (11, 22, 12, 21),
        "Capricornio": (12, 22, 1, 19),
        "Acuario": (1, 20, 2, 18),
        "Piscis": (2, 19, 3, 20)
    }

    for signo, (m1, d1, m2, d2) in signos.items():
        if m1 == m2:
            if mes == m1 and d1 <= dia <= d2:
                return signo
        else:
            if (mes == m1 and dia >= d1) or (mes == m2 and dia <= d2):
                return signo

    return "Desconocido"


def obtener_signo_zodiaco_chino(año):
    """
    Determina el signo del zodíaco chino.

    Args:
        año (int): El año de nacimiento

    Returns:
        str: El signo del zodíaco chino
    """
    signos_chinos = ["Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente",
                     "Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo"]

    indice = (año - 1900) % 12
    return signos_chinos[indice]


def obtener_dia_semana(fecha_nacimiento):
    """
    Obtiene el día de la semana en que nació la persona.

    Args:
        fecha_nacimiento (date): La fecha de nacimiento

    Returns:
        str: El día de la semana
    """
    dias = ["Lunes", "Martes", "Miércoles",
            "Jueves", "Viernes", "Sábado", "Domingo"]
    return dias[fecha_nacimiento.weekday()]


def es_bisiesto(año):
    """
    Verifica si un año es bisiesto.

    Args:
        año (int): El año a verificar

    Returns:
        bool: True si es bisiesto, False en caso contrario
    """
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)


def obtener_estacion(fecha_nacimiento):
    """
    Obtiene la estación del año en que nació la persona.

    Args:
        fecha_nacimiento (date): La fecha de nacimiento

    Returns:
        str: La estación del año
    """
    mes = fecha_nacimiento.month

    if mes in [12, 1, 2]:
        return "Invierno"
    elif mes in [3, 4, 5]:
        return "Primavera"
    elif mes in [6, 7, 8]:
        return "Verano"
    else:
        return "Otoño"


def mostrar_informacion_persona(nombre, fecha_nacimiento):
    """
    Muestra toda la información de una persona.

    Args:
        nombre (str): El nombre de la persona
        fecha_nacimiento (date): La fecha de nacimiento
    """
    edad = calcular_edad(fecha_nacimiento)
    dias_cumple = dias_hasta_cumpleaños(fecha_nacimiento)
    signo_occidental = obtener_signo_zodiaco_occidental(fecha_nacimiento)
    signo_chino = obtener_signo_zodiaco_chino(fecha_nacimiento.year)
    dia_semana = obtener_dia_semana(fecha_nacimiento)
    estacion = obtener_estacion(fecha_nacimiento)
    bisiesto = es_bisiesto(fecha_nacimiento.year)

    print("\n" + "="*60)
    print(f"INFORMACIÓN DE {nombre.upper()}")
    print("="*60)
    print(
        f"Fecha de nacimiento: {fecha_nacimiento.strftime('%d de %B de %Y')}")
    print(f"Día de la semana:    {dia_semana}")
    print(f"Edad actual:         {edad} años")
    print(f"Estación de nacimiento: {estacion}")
    print("-"*60)
    print(f"Zodíaco Occidental:  {signo_occidental}")
    print(f"Zodíaco Chino:       {signo_chino}")
    print("-"*60)
    print(f"Próximo cumpleaños:  En {dias_cumple} días")
    print(f"Año bisiesto:        {'Sí' if bisiesto else 'No'}")
    print("="*60 + "\n")


def validar_fecha(dia, mes, año):
    """
    Valida una fecha ingresada.

    Args:
        dia (int): El día
        mes (int): El mes
        año (int): El año

    Returns:
        bool: True si la fecha es válida
    """
    try:
        date(año, mes, dia)
        return True
    except ValueError:
        return False


def obtener_fecha_nacimiento():
    """
    Obtiene la fecha de nacimiento del usuario con validación.

    Returns:
        date: La fecha de nacimiento validada
    """
    while True:
        try:
            print("\nIngresa tu fecha de nacimiento:")
            dia = int(input("Día (1-31): "))
            mes = int(input("Mes (1-12): "))
            año = int(input("Año (ej: 1990): "))

            if validar_fecha(dia, mes, año):
                fecha = date(año, mes, dia)
                if fecha > date.today():
                    print("Error: La fecha no puede ser en el futuro.")
                    continue
                return fecha
            else:
                print("Error: Fecha inválida. Intenta de nuevo.")
        except ValueError:
            print("Error: Debes ingresar números válidos.")


def menu_principal():
    """Muestra el menú principal."""
    print("\n" + "="*60)
    print("INFORMACIÓN PERSONAL POR FECHA DE NACIMIENTO")
    print("="*60)
    print("1. Buscar información por nombre y fecha de nacimiento")
    print("2. Salir")
    print("="*60)


def main():
    """Función principal del programa."""
    while True:
        menu_principal()
        opcion = input("Selecciona una opción (1-2): ")

        if opcion == "1":
            nombre = input("Ingresa tu nombre: ").strip()
            if nombre:
                fecha_nacimiento = obtener_fecha_nacimiento()
                mostrar_informacion_persona(nombre, fecha_nacimiento)
            else:
                print("Error: Debes ingresar un nombre válido.")

        elif opcion == "2":
            print("\n¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")


if __name__ == "__main__":
    main()
