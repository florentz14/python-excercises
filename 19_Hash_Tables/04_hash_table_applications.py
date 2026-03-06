# -------------------------------------------------
# File: 04_hash_table_applications.py
# Description: Hash Table practical applications.
#              Real-world use cases.
# -------------------------------------------------


# ================================================
# 1. WORD FREQUENCY COUNTER
# ================================================

def count_word_frequency(text):
    """Count frequency of each word using hash table."""
    frequency = {}  # Python dict is a hash table
    words = text.lower().split()
    
    for word in words:
        # Remove punctuation
        word = ''.join(c for c in word if c.isalnum())
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    
    return frequency


# ================================================
# 2. TWO SUM PROBLEM
# ================================================

def two_sum(nums, target):
    """
    Find two numbers that add up to target.
    Returns indices of the two numbers.
    Time: O(n), Space: O(n)
    """
    seen = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return None


# ================================================
# 3. ANAGRAM GROUPING
# ================================================

def group_anagrams(words):
    """Group words that are anagrams of each other."""
    groups = {}
    
    for word in words:
        # Sort letters to create a key
        key = ''.join(sorted(word.lower()))
        groups.setdefault(key, []).append(word)
    
    return list(groups.values())


# ================================================
# 4. LRU CACHE (Least Recently Used)
# ================================================

class LRUCache:
    """LRU Cache using hash table + doubly linked list."""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> value
        self.order = []  # access order
    
    def get(self, key):
        if key not in self.cache:
            return None
        
        # Move to end (most recently used)
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used
            lru_key = self.order.pop(0)
            del self.cache[lru_key]
        
        self.cache[key] = value
        self.order.append(key)
    
    def display(self):
        print(f"Cache (LRU -> MRU): {self.order}")
        print(f"Contents: {self.cache}")


# ================================================
# 5. FIND DUPLICATES
# ================================================

def find_duplicates(nums):
    """Find all duplicate elements in a list."""
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    
    return list(duplicates)


# ================================================
# 6. FIRST NON-REPEATING CHARACTER
# ================================================

def first_non_repeating(s):
    """Find first non-repeating character in a string."""
    count = {}
    
    # Count occurrences
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    # Find first with count 1
    for char in s:
        if count[char] == 1:
            return char
    
    return None


# ================================================
# 7. PHONE BOOK
# ================================================

class PhoneBook:
    """Simple phone book using hash table."""
    
    def __init__(self):
        self.contacts = {}
    
    def add(self, name, phone):
        self.contacts[name.lower()] = phone
    
    def lookup(self, name):
        return self.contacts.get(name.lower(), "Not found")
    
    def delete(self, name):
        if name.lower() in self.contacts:
            del self.contacts[name.lower()]
            return True
        return False
    
    def search(self, prefix):
        """Search contacts by prefix."""
        prefix = prefix.lower()
        return {k: v for k, v in self.contacts.items() if k.startswith(prefix)}


# Example usage
if __name__ == "__main__":
    print("=" * 50)
    print("HASH TABLE APPLICATIONS")
    print("=" * 50)
    
    # 1. Word frequency
    print("\n1. WORD FREQUENCY COUNTER")
    print("-" * 30)
    text = "the quick brown fox jumps over the lazy dog the fox"
    freq = count_word_frequency(text)
    print(f"Text: '{text}'")
    print(f"Frequency: {freq}")
    
    # 2. Two Sum
    print("\n2. TWO SUM PROBLEM")
    print("-" * 30)
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"nums = {nums}, target = {target}")
    print(f"Indices: {result}")
    
    # 3. Group anagrams
    print("\n3. ANAGRAM GROUPING")
    print("-" * 30)
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groups = group_anagrams(words)
    print(f"Words: {words}")
    print(f"Groups: {groups}")
    
    # 4. LRU Cache
    print("\n4. LRU CACHE")
    print("-" * 30)
    cache = LRUCache(3)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    cache.display()
    print(f"Get 'a': {cache.get('a')}")
    cache.display()
    cache.put("d", 4)  # Should evict 'b'
    print("After adding 'd':")
    cache.display()
    
    # 5. Find duplicates
    print("\n5. FIND DUPLICATES")
    print("-" * 30)
    nums = [1, 2, 3, 4, 2, 5, 3, 6]
    dups = find_duplicates(nums)
    print(f"Numbers: {nums}")
    print(f"Duplicates: {dups}")
    
    # 6. First non-repeating
    print("\n6. FIRST NON-REPEATING CHARACTER")
    print("-" * 30)
    s = "aabbcdeeff"
    result = first_non_repeating(s)
    print(f"String: '{s}'")
    print(f"First non-repeating: '{result}'")
    
    # 7. Phone book
    print("\n7. PHONE BOOK")
    print("-" * 30)
    pb = PhoneBook()
    pb.add("John", "555-1234")
    pb.add("Jane", "555-5678")
    pb.add("Jack", "555-9999")
    print(f"Lookup 'John': {pb.lookup('John')}")
    print(f"Search 'ja': {pb.search('ja')}")
