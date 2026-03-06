# -------------------------------------------------
# File Name: 25_advanced_dict_types.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Advanced Dictionary Types.
#              Explores defaultdict (int, list, set, nested) and
#              OrderedDict from the collections module. Includes
#              practical examples: LRU cache simulation, word
#              frequency counter, graph adjacency list, and event log.
# -------------------------------------------------

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
    
    # Demonstrate problem with regular dictionary
    print("1. Problem with Regular Dictionary:")
    print("-" * 60)
    regular_dict = {}
    try:
        # This will raise KeyError because key doesn't exist
        regular_dict['missing_key'] += 1
    except KeyError as e:
        print(f"⚠ KeyError: {e}")
        print("  Regular dict raises error for missing keys")
    print()
    
    # Solution using defaultdict
    print("2. Solution with defaultdict(int):")
    print("-" * 60)
    # Default value is 0 for int type
    count_dict = defaultdict(int)
    # No error - missing key automatically initialized to 0
    count_dict['missing_key'] += 1
    print(f"No error! Value: {count_dict['missing_key']}")
    print(f"Full dict: {dict(count_dict)}")
    print()
    
    # defaultdict with list for grouping data
    print("3. defaultdict(list) - Grouping Data:")
    print("-" * 60)
    # Default value is empty list for list type
    students_by_grade = defaultdict(list)
    
    # Sample student data: (name, grade) tuples
    students = [
        ("Alice", "A"),
        ("Bob", "B"),
        ("Charlie", "A"),
        ("Diana", "C"),
        ("Eve", "B"),
        ("Frank", "A")
    ]
    
    # Group students by grade - missing grades auto-create empty list
    for name, grade in students:
        students_by_grade[grade].append(name)
    
    print("Students grouped by grade:")
    for grade, names in sorted(students_by_grade.items()):
        print(f"  Grade {grade}: {names}")
    print()
    
    # defaultdict with set for unique item collection
    print("4. defaultdict(set) - Unique Items:")
    print("-" * 60)
    # Default value is empty set for set type
    tags_by_post = defaultdict(set)
    
    # Sample post-tag data: (post_id, tag) tuples
    post_tags = [
        ("post1", "python"),
        ("post1", "coding"),
        ("post2", "python"),
        ("post1", "python"),  # Duplicate tag - will be ignored by set
        ("post2", "tutorial"),
        ("post3", "python"),
        ("post3", "advanced")
    ]
    
    # Add tags to sets - duplicates automatically removed
    for post, tag in post_tags:
        tags_by_post[post].add(tag)
    
    print("Tags by post (duplicates removed):")
    for post, tags in sorted(tags_by_post.items()):
        print(f"  {post}: {sorted(tags)}")
    print()
    
    # Nested defaultdict for multi-level grouping
    print("5. Nested defaultdict:")
    print("-" * 60)
    # Track sales by category and month - nested structure
    # Outer dict defaults to defaultdict(int), inner dict defaults to 0
    sales = defaultdict(lambda: defaultdict(int))
    
    # Sample transaction data: (category, month, amount) tuples
    transactions = [
        ("Electronics", "January", 1000),
        ("Electronics", "January", 1500),
        ("Clothing", "January", 800),
        ("Electronics", "February", 2000),
        ("Clothing", "February", 1200),
    ]
    
    # Accumulate sales amounts - auto-creates nested structure as needed
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
    # Create OrderedDict to maintain insertion order
    ordered = OrderedDict()
    ordered['first'] = 1
    ordered['second'] = 2
    ordered['third'] = 3
    
    # Display items in insertion order
    print("Insertion order maintained:")
    for key, value in ordered.items():
        print(f"  {key}: {value}")
    print()
    
    # Demonstrate move_to_end method
    print("2. move_to_end() Method:")
    print("-" * 60)
    # Move 'first' to the end of the dictionary
    ordered.move_to_end('first')
    print("After moving 'first' to end:")
    print(f"  Keys: {list(ordered.keys())}")
    
    # Move 'third' to the beginning (last=False)
    ordered.move_to_end('third', last=False)
    print("After moving 'third' to beginning:")
    print(f"  Keys: {list(ordered.keys())}")
    print()
    
    # LRU Cache simulation
    print("3. Simulating LRU Cache with OrderedDict:")
    print("-" * 60)
    
    class LRUCache:
        """Simple LRU (Least Recently Used) cache."""
        
        def __init__(self, capacity):
            # Use OrderedDict to track access order
            self.cache = OrderedDict()
            self.capacity = capacity
        
        def get(self, key):
            # Return None if key doesn't exist
            if key not in self.cache:
                return None
            # Move accessed key to end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        
        def put(self, key, value):
            # If key exists, update and move to end
            if key in self.cache:
                self.cache.move_to_end(key)
            # Add/update the key-value pair
            self.cache[key] = value
            # Remove oldest entry (first item) if over capacity
            if len(self.cache) > self.capacity:
                oldest = next(iter(self.cache))
                print(f"    Evicting: {oldest}")
                del self.cache[oldest]
        
        def show(self):
            # Return list of keys in order (oldest to newest)
            return list(self.cache.keys())
    
    # Create LRU cache with capacity of 3
    cache = LRUCache(3)
    print("LRU Cache (capacity=3):")
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    print(f"  After adding a,b,c: {cache.show()}")
    
    # Access 'a' - moves it to most recently used position
    cache.get("a")
    print(f"  After accessing 'a': {cache.show()}")
    
    # Adding 'd' will evict 'b' (least recently used)
    cache.put("d", 4)
    print(f"  After adding 'd': {cache.show()}")
    print()
    
    # ========== PART 3: Practical Examples ==========
    print("\nPART 3: Practical Examples")
    print("=" * 60)
    
    # Word frequency counter using defaultdict
    print("1. Word Frequency Counter:")
    print("-" * 60)
    text = "python is great python is fun python is powerful"
    # Default value is 0 for counting
    word_freq = defaultdict(int)
    
    # Count occurrences of each word
    for word in text.split():
        word_freq[word] += 1
    
    print("Word frequencies:")
    for word, count in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print(f"  {word}: {count}")
    print()
    
    # Graph representation using adjacency list
    print("2. Graph with defaultdict(list):")
    print("-" * 60)
    # Default value is empty list for storing neighbors
    graph = defaultdict(list)
    
    # Define graph edges: (start_node, end_node) tuples
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E")
    ]
    
    # Build adjacency list - each node maps to list of neighbors
    for start, end in edges:
        graph[start].append(end)
    
    print("Graph adjacency list:")
    for node, neighbors in sorted(graph.items()):
        print(f"  {node} -> {neighbors}")
    print()
    
    # Event log maintaining chronological order
    print("3. Event Log with OrderedDict:")
    print("-" * 60)
    # OrderedDict preserves insertion order for chronological events
    event_log = OrderedDict()
    
    # Sample events: (timestamp, event_description) tuples
    events = [
        ("09:00", "System started"),
        ("09:15", "User logged in"),
        ("10:30", "File uploaded"),
        ("11:45", "Report generated"),
        ("12:00", "User logged out")
    ]
    
    # Store events in chronological order
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
