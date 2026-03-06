# -------------------------------------------------
# File Name: 15_set_comprehension.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Set Comprehension (Determination by Comprehension).
#              Creates sets using comprehension syntax with
#              conditions: even numbers, solutions to x²=16,
#              and vowels extracted from a word.
# -------------------------------------------------

"""
Exercise 2: Set Comprehension
This exercise shows how to create sets using comprehension and conditions.
"""

def main():
    print("Exercise 2: Determination by Comprehension")
    print("=" * 50)
    
    # a) B = {x | x is an even number less than 15}
    # Using set comprehension to generate even numbers
    # The condition x % 2 == 0 filters for even numbers
    B = {x for x in range(0, 15) if x % 2 == 0}
    print(f"a) B = {{x | x is an even number less than 15}}")
    print(f"   B = {sorted(B)}")
    print()
    
    # b) C = {x | x² = 16}
    # Finding all numbers whose square equals 16
    # We check numbers from -20 to 20 to find solutions
    # Note: Both 4 and -4 satisfy x² = 16
    C = {x for x in range(-20, 21) if x ** 2 == 16}
    print(f"b) C = {{x | x² = 16}}")
    print(f"   C = {sorted(C)}")
    print()
    
    # c) D = {x | x is a vowel in the word "matemáticas"}
    # Extracting unique vowels from the word
    # The set automatically removes duplicates
    word = "matemáticas"
    # Define set of vowels including accented characters
    vowels = {'a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú'}
    # Filter characters that are vowels (case-insensitive)
    D = {char for char in word if char.lower() in vowels}
    print(f"c) D = {{x | x is a vowel in the word 'matemáticas'}}")
    print(f"   D = {sorted(D)}")
    
    print("\n" + "=" * 50)
    print("Explanation:")
    print("  - Set comprehension allows us to create sets based on conditions")
    print("  - The syntax is: {expression for item in iterable if condition}")
    print("  - Sets automatically remove duplicate elements")


if __name__ == "__main__":
    main()
