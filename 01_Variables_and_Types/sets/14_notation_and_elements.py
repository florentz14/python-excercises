# -------------------------------------------------
# File Name: 14_notation_and_elements.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Set Notation and Elements.
#              Demonstrates set membership testing (in / not in)
#              and subset checking with issubset(). Verifies
#              whether specific values belong to a defined set.
# -------------------------------------------------

"""
Exercise 1: Set Notation and Elements
This exercise demonstrates set membership and subset operations in Python.
"""

def main():
    # Define set A with specific elements
    A = {2, 4, 6, 8, 10}
    
    print("Exercise 1: Notation and Elements")
    print("=" * 50)
    print(f"Set A = {A}")
    print()
    
    # a) Check if 6 is an element of A (6 ∈ A)
    # Using the 'in' operator to test membership
    result_a = 6 in A
    print(f"a) Is 6 ∈ A? {result_a}")
    
    # b) Check if 5 is an element of A (5 ∈ A)
    # Testing membership for an element not in the set
    result_b = 5 in A
    print(f"b) Is 5 ∈ A? {result_b}")
    
    # c) Check if 10 is NOT an element of A (10 ∉ A)
    # Using 'not in' operator to verify non-membership
    result_c = 10 not in A
    print(f"c) Is 10 ∉ A? {result_c}")
    
    # d) Check if {2, 4} is a subset of A ({2, 4} ⊂ A)
    # Using issubset() method to verify subset relationship
    subset = {2, 4}
    result_d = subset.issubset(A)
    print(f"d) Is {{2, 4}} ⊂ A? {result_d}")
    
    print("\n" + "=" * 50)
    print("Summary:")
    print(f"  a) TRUE  - 6 is in set A")
    print(f"  b) FALSE - 5 is not in set A")
    print(f"  c) FALSE - 10 IS in set A")
    print(f"  d) TRUE  - {{2, 4}} is a subset of A")


if __name__ == "__main__":
    main()
