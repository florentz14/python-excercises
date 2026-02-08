"""
Exercise 9: Advanced Dictionary Types
This exercise explores specialized dictionary types from the collections module.
DefaultDict and OrderedDict provide enhanced functionality for specific use cases.
"""

from collections import defaultdict, OrderedDict, Counter
from datetime import datetime


def main():
    print("Exercise 9: Advanced Dictionary Types")
    print("=" * 60)
    
    # ========== PART 1: defaultdict ==========
    print("\nPART 1: defaultdict")
    print("=" * 60)
    
    # Problem with regular dict
    print("1. Problem with Regular Dictionary:")
    print("-" * 60)
    regular_dict = {}
    try:
        regular_dict['missing_key'] += 1
    except KeyError as e:
        print(f"⚠ KeyError: {e}")
        print("  Regular dict raises error for missing keys")
    print()
    
    # Solution with defaultdict
    print("2. Solution with defaultdict(int):")
    print("-" * 60)
    count_dict = defaultdict(int)  # Default value is 0
    count_dict['missing_key'] += 1
    print(f"No error! Value: {count_dict['missing_key']}")
    print(f"Full dict: {dict(count_dict)}")
    print()
    
    # defaultdict with list
    print("3. defaultdict(list) - Grouping Data:")
    print("-" * 60)
    students_by_grade = defaultdict(list)
    
    students = [
        ("Alice", "A"),
        ("Bob", "B"),
        ("Charlie", "A"),
        ("Diana", "C"),
        ("Eve", "B"),
        ("Frank", "A")
    ]
    
    # Group students by grade
    for name, grade in students:
        students_by_grade[grade].append(name)
    
    print("Students grouped by grade:")
    for grade, names in sorted(students_by_grade.items()):
        print(f"  Grade {grade}: {names}")
    print()
    
    # defaultdict with set
    print("4. defaultdict(set) - Unique Items:")
    print("-" * 60)
    tags_by_post = defaultdict(set)
    
    post_tags = [
        ("post1", "python"),
        ("post1", "coding"),
        ("post2", "python"),
        ("post1", "python"),  # Duplicate
        ("post2", "tutorial"),
        ("post3", "python"),
        ("post3", "advanced")
    ]
    
    for post, tag in post_tags:
        tags_by_post[post].add(tag)
    
    print("Tags by post (duplicates removed):")
    for post, tags in sorted(tags_by_post.items()):
        print(f"  {post}: {sorted(tags)}")
    print()
    
    # Nested defaultdict
    print("5. Nested defaultdict:")
    print("-" * 60)
    # Track sales by category and month
    sales = defaultdict(lambda: defaultdict(int))
    
    transactions = [
        ("Electronics", "January", 1000),
        ("Electronics", "January", 1500),
        ("Clothing", "January", 800),
        ("Electronics", "February", 2000),
        ("Clothing", "February", 1200),
    ]
    
    for category, month, amount in transactions:
        sales[category][month] += amount
    
    print("Sales by category and month:")
    for category, months in sales.items():
        print(f"\n{category}:")
        for month, total in months.items():
            print(f"  {month}: ${total}")
    print()
    
    # ========== PART 2: OrderedDict ==========
    print("\nPART 2: OrderedDict")
    print("=" * 60)
    print("NOTE: In Python 3.7+, regular dicts maintain insertion order.")
    print("OrderedDict has additional methods and guarantees order.")
    print()
    
    print("1. Basic OrderedDict Usage:")
    print("-" * 60)
    ordered = OrderedDict()
    ordered['first'] = 1
    ordered['second'] = 2
    ordered['third'] = 3
    
    print("Insertion order maintained:")
    for key, value in ordered.items():
        print(f"  {key}: {value}")
    print()
    
    # move_to_end method
    print("2. move_to_end() Method:")
    print("-" * 60)
    ordered.move_to_end('first')  # Move to end
    print("After moving 'first' to end:")
    print(f"  Keys: {list(ordered.keys())}")
    
    ordered.move_to_end('third', last=False)  # Move to beginning
    print("After moving 'third' to beginning:")
    print(f"  Keys: {list(ordered.keys())}")
    print()
    
    # LRU Cache simulation
    print("3. Simulating LRU Cache with OrderedDict:")
    print("-" * 60)
    
    class LRUCache:
        """Simple LRU (Least Recently Used) cache."""
        
        def __init__(self, capacity):
            self.cache = OrderedDict()
            self.capacity = capacity
        
        def get(self, key):
            if key not in self.cache:
                return None
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        
        def put(self, key, value):
            if key in self.cache:
                # Update and move to end
                self.cache.move_to_end(key)
            self.cache[key] = value
            # Remove oldest if over capacity
            if len(self.cache) > self.capacity:
                oldest = next(iter(self.cache))
                print(f"    Evicting: {oldest}")
                del self.cache[oldest]
        
        def show(self):
            return list(self.cache.keys())
    
    cache = LRUCache(3)
    print("LRU Cache (capacity=3):")
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    print(f"  After adding a,b,c: {cache.show()}")
    
    cache.get("a")  # Access 'a'
    print(f"  After accessing 'a': {cache.show()}")
    
    cache.put("d", 4)  # This will evict 'b'
    print(f"  After adding 'd': {cache.show()}")
    print()
    
    # ========== PART 3: Practical Examples ==========
    print("\nPART 3: Practical Examples")
    print("=" * 60)
    
    # Word frequency with defaultdict
    print("1. Word Frequency Counter:")
    print("-" * 60)
    text = "python is great python is fun python is powerful"
    word_freq = defaultdict(int)
    
    for word in text.split():
        word_freq[word] += 1
    
    print("Word frequencies:")
    for word, count in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print(f"  {word}: {count}")
    print()
    
    # Graph representation
    print("2. Graph with defaultdict(list):")
    print("-" * 60)
    graph = defaultdict(list)
    
    # Add edges
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E")
    ]
    
    for start, end in edges:
        graph[start].append(end)
    
    print("Graph adjacency list:")
    for node, neighbors in sorted(graph.items()):
        print(f"  {node} -> {neighbors}")
    print()
    
    # Event log with OrderedDict
    print("3. Event Log with OrderedDict:")
    print("-" * 60)
    event_log = OrderedDict()
    
    events = [
        ("09:00", "System started"),
        ("09:15", "User logged in"),
        ("10:30", "File uploaded"),
        ("11:45", "Report generated"),
        ("12:00", "User logged out")
    ]
    
    for time, event in events:
        event_log[time] = event
    
    print("Event timeline (chronological):")
    for time, event in event_log.items():
        print(f"  {time} - {event}")
    
    print("\n" + "=" * 60)
    print("Summary:")
    print("  defaultdict:")
    print("    - Provides default value for missing keys")
    print("    - Great for counting, grouping, collecting")
    print("    - Common types: int, list, set, dict")
    print()
    print("  OrderedDict:")
    print("    - Maintains insertion order (like dict in 3.7+)")
    print("    - Has move_to_end() method")
    print("    - Useful for LRU caches, ordered logs")


if __name__ == "__main__":
    main()
