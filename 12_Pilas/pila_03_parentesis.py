"""
Pilas - Ejemplo 3: Balanceo de paréntesis
==========================================
Tema: 12_Pilas
Descripción: Usar pila para verificar si ( ) [ ] { } están balanceados.
"""

def balanceado(s):
    pila = []
    pares = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c in "([{":
            pila.append(c)
        elif c in ")]}":
            if not pila or pila[-1] != pares[c]:
                return False
            pila.pop()
    return len(pila) == 0


print(balanceado("(2+3)*[4-1]"))   # True
print(balanceado("((())"))          # False
print(balanceado("{[()]}"))         # True
print(balanceado("{[)]}"))          # False
