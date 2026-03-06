# -------------------------------------------------
# File Name: 17_intersection.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Intersection of Sets.
#              Computes P ∩ Q using the & operator or
#              intersection() method. Checks if the result is
#              empty (disjoint) and explains the concept.
# -------------------------------------------------

"""
Exercise 4: Intersection of Sets
This exercise demonstrates the intersection operation between sets.
The intersection contains only elements present in both sets.
"""

def main():
    # Define two sets with some common elements
    P = {'a', 'e', 'i', 'o', 'u'}
    Q = {'a', 'b', 'c', 'd', 'e'}
    
    print("Exercise 4: Intersection of Sets")
    print("=" * 50)
    print(f"Set P = {sorted(P)}")
    print(f"Set Q = {sorted(Q)}")
    print()
    
    # a) Calculate P ∩ Q (intersection of P and Q)
    # The intersection operator & or the intersection() method can be used
    # Intersection contains only elements present in BOTH sets
    intersection_PQ = P & Q  # Alternative: P.intersection(Q)
    print(f"a) P ∩ Q = {sorted(intersection_PQ)}")
    print()
    
    # b) Check if the intersection is empty and explain
    # Empty intersection means the sets are disjoint (no common elements)
    is_empty = len(intersection_PQ) == 0
    print(f"b) Is P ∩ Q = ∅ (empty set)? {is_empty}")
    
    if is_empty:
        print("   Meaning: The sets are disjoint (no common elements)")
    else:
        print("   Meaning: The sets have common elements")
        print(f"   Common elements: {sorted(intersection_PQ)}")
    
    print("\n" + "=" * 50)
    print("Explanation:")
    print("  - The intersection (∩) contains only elements in BOTH sets")
    print("  - If P ∩ Q = ∅, the sets would be called 'disjoint'")
    print(f"  - In this case, P and Q share {len(intersection_PQ)} element(s)")
    print("  - The empty set ∅ is represented as set() in Python")


if __name__ == "__main__":
    main()
