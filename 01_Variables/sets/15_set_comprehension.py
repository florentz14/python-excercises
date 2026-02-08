"""
Exercise 2: Set Comprehension
This exercise shows how to create sets using comprehension and conditions.
"""

def main():
    print("Exercise 2: Determination by Comprehension")
    print("=" * 50)
    
    # a) B = {x | x is an even number less than 15}
    # Using set comprehension to generate even numbers
    B = {x for x in range(0, 15) if x % 2 == 0}
    print(f"a) B = {{x | x is an even number less than 15}}")
    print(f"   B = {sorted(B)}")
    print()
    
    # b) C = {x | x² = 16}
    # Finding all numbers whose square equals 16
    # We check numbers from -20 to 20 to find solutions
    C = {x for x in range(-20, 21) if x ** 2 == 16}
    print(f"b) C = {{x | x² = 16}}")
    print(f"   C = {sorted(C)}")
    print()
    
    # c) D = {x | x is a vowel in the word "matemáticas"}
    # Extracting unique vowels from the word
    word = "matemáticas"
    vowels = {'a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú'}
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
