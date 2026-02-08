# -------------------------------------------------
# File Name: 17_pila.py
# Author: Florentino Báez
# Date: Variables - Lists
# Description: List as a Stack (LIFO).
#              Last In, First Out. Use append() to push
#              and pop() to remove from the top. Peek
#              with list[-1] without removing.
# -------------------------------------------------

print("=== List as a stack (LIFO) ===")
print("Operations: append() to push, pop() to remove from top")
print()

pila = []
print(f"Empty stack: {pila}")

# Push — add to the top (end of list)
pila.append(1)
pila.append(2)
pila.append(3)
print(f"After append(1), append(2), append(3): {pila}")

# Pop — remove from the top (end of list)
ultimo = pila.pop()
print(f"pop() returns: {ultimo}")
print(f"Stack after pop: {pila}")

# More push/pop operations
pila.append(4)
pila.append(5)
print(f"After append(4), append(5): {pila}")

print(f"pop(): {pila.pop()}")
print(f"pop(): {pila.pop()}")
print(f"Final stack: {pila}")

# Peek — view the top element without removing it
print(f"\nPeek (top without removing): pila[-1] = {pila[-1]}")
