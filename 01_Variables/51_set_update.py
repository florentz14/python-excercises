# Example 14: Set operations with methods
print("Example 14: Set operations with methods")
print("-" * 40)
set_p = {1, 2, 3}
set_q = {3, 4, 5}
print("Set P:", set_p)
print("Set Q:", set_q)
set_p.update(set_q)  # Add all elements from set_q
print("After P.update(Q):", set_p)
