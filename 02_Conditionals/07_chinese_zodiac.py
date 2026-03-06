"""
Ejercicio: Zodíaco Chino

Programa que determina el signo del zodíaco chino según el año de nacimiento.
"""

# Diccionario con los signos del zodíaco chino y sus características
zodiac_signs = {
    "Rata": {
        "años": [1900, 1912, 1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020],
        "características": "Inteligente, rápida, adaptable, sociable",
        "elemento": "Agua, Fuego, Madera, Metal, Tierra"
    },
    "Buey": {
        "años": [1901, 1913, 1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021],
        "características": "Fuerte, confiable, trabajador, paciente",
        "elemento": "Agua, Fuego, Madera, Metal, Tierra"
    },
    "Tigre": {
        "años": [1902, 1914, 1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022],
        "características": "Valiente, apasionado, competitivo, impulsivo",
        "elemento": "Agua, Fuego, Madera, Metal, Tierra"
    },
    "Conejo": {
        "años": [1903, 1915, 1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023],
        "características": "Gentil, amable, tranquilo, prudente",
        "elemento": "Agua, Fuego, Madera, Metal, Tierra"
    },
    "Dragón": {
        "años": [1904, 1916, 1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024],
        "características": "Poderoso, afortunado, carismático, dominante",
        "elemento": "Agua, Fuego, Madera, Metal, Tierra"
    },
    "Serpiente": {
        "años": [1905, 1917, 1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025],
        "características": "Sabia, misteriosa, intuitiva, elegante",
        "elemento": "Agua, Fuego, Madera, Metal, Tierra"
    },
    "Caballo": {
        "años": [1906, 1918, 1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014],
        "características": "Energético, aventurero, libre, sincero",
        "elemento": "Agua, Fuego, Madera, Metal, Tierra"
    },
    "Cabra": {
        "años": [1907, 1919, 1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015],
        "características": "Sensible, artístico, tranquilo, dependiente",
        "elemento": "Agua, Fuego, Madera, Metal, Tierra"
    },
    "Mono": {
        "años": [1908, 1920, 1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016],
        "características": "Ingenioso, juguetón, versátil, impredecible",
        "elemento": "Agua, Fuego, Madera, Metal, Tierra"
    },
    "Gallo": {
        "años": [1909, 1921, 1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017],
        "características": "Honesto, directo, valiente, independiente",
        "elemento": "Agua, Fuego, Madera, Metal, Tierra"
    },
    "Perro": {
        "años": [1910, 1922, 1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018],
        "características": "Leal, honesto, protector, confiable",
        "elemento": "Agua, Fuego, Madera, Metal, Tierra"
    },
    "Cerdo": {
        "años": [1911, 1923, 1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019],
        "características": "Generoso, compasivo, sincero, ingenuo",
        "elemento": "Agua, Fuego, Madera, Metal, Tierra"
    }
}


def obtener_signo_zodiacal(año):
    """
    Determina el signo del zodíaco chino para un año dado.

    Args:
        año (int): El año de nacimiento

    Returns:
        str: El signo del zodíaco chino
    """
    for signo, datos in zodiac_signs.items():
        if año in datos["años"]:
            return signo
    return None


def mostrar_informacion_signo(signo):
    """
    Muestra la información detallada de un signo del zodíaco.

    Args:
        signo (str): El nombre del signo
    """
    if signo in zodiac_signs:
        info = zodiac_signs[signo]
        print(f"\n{'='*50}")
        print(f"SIGNO: {signo.upper()}")
        print(f"{'='*50}")
        print(f"Características: {info['características']}")
        print(f"Años: {', '.join(map(str, info['años']))}")
        print(f"{'='*50}\n")
    else:
        print("Signo no encontrado.")


def mostrar_todos_signos():
    """Muestra todos los signos del zodíaco chino."""
    print("\n" + "="*50)
    print("SIGNOS DEL ZODÍACO CHINO")
    print("="*50)
    for i, signo in enumerate(zodiac_signs.keys(), 1):
        print(f"{i:2}. {signo}")
    print("="*50 + "\n")


def menu_principal():
    """Muestra el menú principal."""
    print("\n" + "="*50)
    print("ZODÍACO CHINO")
    print("="*50)
    print("1. Buscar mi signo por año de nacimiento")
    print("2. Ver información de un signo")
    print("3. Ver todos los signos")
    print("4. Salir")
    print("="*50)


def main():
    """Función principal del programa."""
    while True:
        menu_principal()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            try:
                año = int(input("Ingresa tu año de nacimiento: "))
                if año < 1900:
                    print("Por favor, ingresa un año a partir de 1900.")
                else:
                    signo = obtener_signo_zodiacal(año)
                    if signo:
                        print(f"\nTu signo del zodíaco chino es: {signo}")
                        mostrar_informacion_signo(signo)
                    else:
                        print(
                            "Año no encontrado en la base de datos del zodíaco chino.")
            except ValueError:
                print("Error: Debes ingresar un número válido.")

        elif opcion == "2":
            mostrar_todos_signos()
            signo = input(
                "Ingresa el nombre del signo (ej: Rata, Tigre, Dragón): ").capitalize()
            mostrar_informacion_signo(signo)

        elif opcion == "3":
            mostrar_todos_signos()
            for signo in zodiac_signs.keys():
                info = zodiac_signs[signo]
                print(f"{signo:10} - {info['características']}")
            print()

        elif opcion == "4":
            print("\n¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")


if __name__ == "__main__":
    main()
