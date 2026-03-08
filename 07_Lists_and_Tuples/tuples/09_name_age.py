# -------------------------------------------------
# File Name: 09_name_age.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Pedir nombre y edad al usuario, guardarlos en una tupla
# -------------------------------------------------

name = input('Enter your name: ')
# Convertimos la entrada a entero para la edad
age = int(input('Enter your age: '))
# Creamos una tupla con los dos valores
info = (name, age)
# Mostramos la tupla (nombre, edad)
print(info)
