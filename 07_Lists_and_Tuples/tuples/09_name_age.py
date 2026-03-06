# ---------------------------------------------------------------------------
# Part 2: Tuples - Exercise 9
# ---------------------------------------------------------------------------
# Descripción: Pedir nombre y edad al usuario, guardarlos en una tupla
#              y mostrar la tupla. input() lee texto; int() convierte la edad.
# ---------------------------------------------------------------------------

# input() devuelve una cadena; la guardamos en name
name = input('Enter your name: ')
# Convertimos la entrada a entero para la edad
age = int(input('Enter your age: '))
# Creamos una tupla con los dos valores
info = (name, age)
# Mostramos la tupla (nombre, edad)
print(info)
