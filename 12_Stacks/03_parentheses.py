# -------------------------------------------------
# File Name: 03_parentheses.py
# Author: Florentino Báez
# Date: 12_Stacks
# Description: Parenthesis balancing. Stack verifies ( ) [ ] { } are balanced.
# -------------------------------------------------

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
