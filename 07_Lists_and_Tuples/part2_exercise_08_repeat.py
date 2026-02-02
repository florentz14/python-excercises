# ---------------------------------------------------------------------------
# Part 2: Tuples - Exercise 8
# ---------------------------------------------------------------------------
# Descripción: Repetir una tupla n veces con el operador *. La coma en
#              ('Hi',) es necesaria para que Python la reconozca como tupla.
# ---------------------------------------------------------------------------

# Tupla de un solo elemento (la coma la define como tupla, no como string)
greet = ('Hi',)
# * 4 repite la tupla 4 veces: ('Hi', 'Hi', 'Hi', 'Hi')
print(greet * 4)
