"""
Exercise 4: Dictionary Comprehension
This exercise demonstrates how to create dictionaries using comprehension syntax.
Dictionary comprehension provides a concise way to create dictionaries from iterables.
"""

def main():
    print("Exercise 4: Dictionary Comprehension")
    print("=" * 60)
    
    # 1. Basic dictionary comprehension
    print("1. Basic Dictionary Comprehension:")
    print("-" * 60)
    # Create a dictionary of squares
    squares = {x: x**2 for x in range(1, 6)}
    print(f"Squares: {squares}")
    print("Comprehension: {x: x**2 for x in range(1, 6)}")
    print()
    
    # 2. Dictionary comprehension with condition
    print("2. With Conditional Filter:")
    print("-" * 60)
    # Only even numbers
    even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
    print(f"Even squares: {even_squares}")
    print("Comprehension: {x: x**2 for x in range(1, 11) if x % 2 == 0}")
    print()
    
    # 3. Creating dictionary from two lists
    print("3. Creating Dictionary from Two Lists:")
    print("-" * 60)
    names = ["Alice", "Bob", "Charlie", "Diana"]
    scores = [85, 92, 78, 95]
    student_scores = {name: score for name, score in zip(names, scores)}
    print(f"Student scores: {student_scores}")
    print()
    
    # 4. String manipulation with comprehension
    print("4. String Manipulation:")
    print("-" * 60)
    words = ["hello", "world", "python", "dictionary"]
    word_lengths = {word: len(word) for word in words}
    print(f"Word lengths: {word_lengths}")
    
    # Uppercase keys
    uppercase_dict = {word.upper(): len(word) for word in words}
    print(f"Uppercase keys: {uppercase_dict}")
    print()
    
    # 5. Transforming existing dictionary
    print("5. Transforming Existing Dictionary:")
    print("-" * 60)
    prices = {"apple": 1.5, "banana": 0.8, "orange": 2.0, "grape": 3.5}
    print(f"Original prices: {prices}")
    
    # Apply 10% discount
    discounted = {item: price * 0.9 for item, price in prices.items()}
    print(f"10% discount: {discounted}")
    
    # Filter expensive items (> $2)
    expensive = {item: price for item, price in prices.items() if price > 2}
    print(f"Expensive items (>$2): {expensive}")
    print()
    
    # 6. Swapping keys and values
    print("6. Swapping Keys and Values:")
    print("-" * 60)
    country_capital = {
        "USA": "Washington DC",
        "UK": "London",
        "France": "Paris",
        "Japan": "Tokyo"
    }
    print(f"Country → Capital: {country_capital}")
    
    capital_country = {capital: country for country, capital in country_capital.items()}
    print(f"Capital → Country: {capital_country}")
    print()
    
    # 7. Nested comprehension
    print("7. Nested Dictionary Comprehension:")
    print("-" * 60)
    # Create multiplication table
    mult_table = {
        i: {j: i * j for j in range(1, 4)}
        for i in range(1, 4)
    }
    print("Multiplication table (1-3):")
    for key, value in mult_table.items():
        print(f"  {key}: {value}")
    print()
    
    # 8. Conditional values
    print("8. Conditional Values in Comprehension:")
    print("-" * 60)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Classify as "even" or "odd"
    number_types = {
        num: "even" if num % 2 == 0 else "odd"
        for num in numbers
    }
    print(f"Number classifications: {number_types}")
    print()
    
    # 9. From enumerate
    print("9. Using enumerate() in Comprehension:")
    print("-" * 60)
    fruits = ["apple", "banana", "cherry", "date"]
    fruit_index = {fruit: index for index, fruit in enumerate(fruits)}
    print(f"Fruit indices: {fruit_index}")
    print()
    
    # 10. Complex example - grade statistics
    print("10. Complex Example - Grade Statistics:")
    print("-" * 60)
    students = [
        ("Alice", [85, 90, 88]),
        ("Bob", [78, 82, 80]),
        ("Charlie", [92, 95, 93]),
        ("Diana", [88, 85, 90])
    ]
    
    # Calculate average for each student
    averages = {
        name: sum(grades) / len(grades)
        for name, grades in students
    }
    print("Student averages:")
    for name, avg in averages.items():
        print(f"  {name}: {avg:.2f}")
    
    print("\n" + "=" * 60)
    print("Dictionary Comprehension Syntax:")
    print("  Basic:      {key: value for item in iterable}")
    print("  Filter:     {key: value for item in iterable if condition}")
    print("  Transform:  {key_expr: value_expr for item in iterable}")
    print("  From zip:   {k: v for k, v in zip(keys, values)}")
    print("  Nested:     {k: {k2: v2 for ...} for k in iterable}")


if __name__ == "__main__":
    main()
