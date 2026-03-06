# -------------------------------------------------
# File Name: 23_venn_diagram.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Venn Diagram Problem — Language Students.
#              Solves a real-world problem using set theory:
#              given total students, English, French, and both,
#              calculates only-English, only-French, and neither.
#              Includes an ASCII Venn diagram.
# -------------------------------------------------

"""
Exercise 10: Venn Diagram Problem
This exercise solves a real-world problem using set theory and the inclusion-exclusion principle.
We use sets to analyze student enrollment in language courses.
"""

def draw_simple_venn():
    """
    Draw a simple ASCII representation of the Venn diagram.
    """
    print("\n   Venn Diagram Representation:")
    print("   " + "=" * 40)
    print("   ")
    print("           English (E)      French (F)")
    print("              _______________")
    print("             /       |       \\")
    print("            /  10    | 8     \\")
    print("           /   only  |both   \\")
    print("          |    E     | E&F    |   7 only F")
    print("           \\         |       /")
    print("            \\_______|______/")
    print("   ")
    print("              5 students study neither")
    print("   " + "=" * 40)


def main():
    # Given data: problem setup with total students and language enrollments
    total_students = 30  # Universal set: all students in the class
    study_english = 18  # Students studying English (includes those studying both)
    study_french = 15  # Students studying French (includes those studying both)
    study_both = 8  # Students studying both languages (intersection)
    
    print("Exercise 10: Venn Diagram - Language Students")
    print("=" * 50)
    print("Problem Setup:")
    print(f"  - Total students in class: {total_students}")
    print(f"  - Students studying English: {study_english}")
    print(f"  - Students studying French: {study_french}")
    print(f"  - Students studying BOTH languages: {study_both}")
    print()
    
    # a) Students studying only English
    # Subtract the intersection (both) from total English students
    only_english = study_english - study_both
    print(f"a) Students studying ONLY English:")
    print(f"   Only English = Total English - Both")
    print(f"   Only English = {study_english} - {study_both} = {only_english}")
    print()
    
    # b) Students studying only French
    # Subtract the intersection (both) from total French students
    only_french = study_french - study_both
    print(f"b) Students studying ONLY French:")
    print(f"   Only French = Total French - Both")
    print(f"   Only French = {study_french} - {study_both} = {only_french}")
    print()
    
    # c) Students studying neither language
    # First, find total students studying at least one language
    # This is the union of English and French sets
    at_least_one = only_english + only_french + study_both  # Union: all language students
    neither = total_students - at_least_one  # Complement: students not in the union
    
    print(f"c) Students studying NEITHER language:")
    print(f"   Step 1: Students studying at least one language")
    print(f"           = Only English + Only French + Both")
    print(f"           = {only_english} + {only_french} + {study_both} = {at_least_one}")
    print(f"   Step 2: Students studying neither")
    print(f"           = Total - At least one")
    print(f"           = {total_students} - {at_least_one} = {neither}")
    
    # Draw the Venn diagram
    draw_simple_venn()
    
    print("\n" + "=" * 50)
    print("Summary:")
    print(f"  - Only English: {only_english} students")
    print(f"  - Only French: {only_french} students")
    print(f"  - Both languages: {study_both} students")
    print(f"  - Neither language: {neither} students")
    print(f"  - Total: {only_english} + {only_french} + {study_both} + {neither} = {only_english + only_french + study_both + neither}")
    
    print("\n" + "=" * 50)
    print("Set Theory Notation:")
    print("  Let E = set of students studying English")
    print("  Let F = set of students studying French")
    print(f"  |E| = {study_english}")
    print(f"  |F| = {study_french}")
    print(f"  |E ∩ F| = {study_both}")
    print(f"  |E ∪ F| = |E| + |F| - |E ∩ F| = {study_english} + {study_french} - {study_both} = {at_least_one}")
    print(f"  |Neither| = |U| - |E ∪ F| = {total_students} - {at_least_one} = {neither}")


if __name__ == "__main__":
    main()
