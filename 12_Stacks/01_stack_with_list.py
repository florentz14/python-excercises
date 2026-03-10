# -------------------------------------------------
# File Name: 01_stack_with_list.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Stack with list (LIFO). append()=push, pop()=pop. Last in, first out.
# -------------------------------------------------

stack = []

# Push: add at the end
stack.append(1)
stack.append(2)
stack.append(3)
print("After push 1, 2, 3:", stack)

# Pop: remove the last item
top = stack.pop()
print("Pop:", top, "-> Stack:", stack)
print("Pop:", stack.pop(), "-> Stack:", stack)

# Peek: view top without removing
if stack:
    print("Top (without removing):", stack[-1])
