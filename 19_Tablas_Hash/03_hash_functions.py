# -------------------------------------------------
# File: 03_hash_functions.py
# Description: Common Hash Functions.
#              Different hashing techniques.
# -------------------------------------------------


def division_hash(key, size):
    """
    Division method: h(k) = k mod m
    Simple and fast, works well when m is prime.
    """
    if isinstance(key, str):
        key = sum(ord(c) for c in key)
    return key % size


def multiplication_hash(key, size, A=0.6180339887):
    """
    Multiplication method: h(k) = floor(m * (k*A mod 1))
    A is typically (sqrt(5) - 1) / 2 ≈ 0.618 (golden ratio)
    """
    if isinstance(key, str):
        key = sum(ord(c) for c in key)
    return int(size * ((key * A) % 1))


def polynomial_hash(s, base=31, mod=10**9 + 7):
    """
    Polynomial rolling hash for strings.
    h = s[0] + s[1]*base + s[2]*base^2 + ...
    """
    hash_value = 0
    power = 1
    for char in s:
        hash_value = (hash_value + ord(char) * power) % mod
        power = (power * base) % mod
    return hash_value


def djb2_hash(s):
    """
    DJB2 hash function by Dan Bernstein.
    Popular string hash function.
    """
    hash_value = 5381
    for char in s:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
        hash_value = hash_value & 0xFFFFFFFF  # Keep it 32-bit
    return hash_value


def fnv1a_hash(s):
    """
    FNV-1a hash function.
    Fast and good distribution.
    """
    FNV_PRIME = 16777619
    FNV_OFFSET = 2166136261
    
    hash_value = FNV_OFFSET
    for char in s:
        hash_value ^= ord(char)
        hash_value = (hash_value * FNV_PRIME) & 0xFFFFFFFF
    return hash_value


def simple_sum_hash(s, size):
    """
    Simple sum of ASCII values.
    Poor distribution, for demonstration only.
    """
    return sum(ord(c) for c in s) % size


def position_weighted_hash(s, size):
    """
    Position-weighted hash.
    Takes character position into account.
    """
    hash_value = 0
    for i, char in enumerate(s):
        hash_value += ord(char) * (i + 1)
    return hash_value % size


def universal_hash(key, size, a, b, p):
    """
    Universal hashing: h(k) = ((a*k + b) mod p) mod m
    a, b are random, p is a prime > m
    """
    if isinstance(key, str):
        key = sum(ord(c) for c in key)
    return ((a * key + b) % p) % size


# Example usage
if __name__ == "__main__":
    print("=" * 50)
    print("HASH FUNCTIONS COMPARISON")
    print("=" * 50)
    
    test_keys = ["apple", "banana", "cherry", "date", "elderberry"]
    table_size = 10
    
    print(f"\nTable size: {table_size}")
    print(f"Test keys: {test_keys}")
    
    # Division hash
    print("\n1. Division Hash:")
    for key in test_keys:
        h = division_hash(key, table_size)
        print(f"   '{key}' -> {h}")
    
    # Multiplication hash
    print("\n2. Multiplication Hash:")
    for key in test_keys:
        h = multiplication_hash(key, table_size)
        print(f"   '{key}' -> {h}")
    
    # Polynomial hash
    print("\n3. Polynomial Hash (full value):")
    for key in test_keys:
        h = polynomial_hash(key)
        print(f"   '{key}' -> {h}")
    
    # DJB2 hash
    print("\n4. DJB2 Hash:")
    for key in test_keys:
        h = djb2_hash(key)
        print(f"   '{key}' -> {h}")
    
    # FNV-1a hash
    print("\n5. FNV-1a Hash:")
    for key in test_keys:
        h = fnv1a_hash(key)
        print(f"   '{key}' -> {h}")
    
    # Position-weighted hash
    print("\n6. Position-weighted Hash:")
    for key in test_keys:
        h = position_weighted_hash(key, table_size)
        print(f"   '{key}' -> {h}")
    
    # Collision comparison
    print("\n" + "=" * 50)
    print("COLLISION ANALYSIS")
    print("=" * 50)
    
    words = ["cat", "act", "tac", "dog", "god", "bat", "tab"]
    
    print(f"\nTest words (anagrams): {words}")
    
    print("\n- Simple sum (many collisions):")
    buckets = {}
    for word in words:
        h = simple_sum_hash(word, table_size)
        buckets.setdefault(h, []).append(word)
        print(f"  '{word}' -> {h}")
    print(f"  Collisions: {sum(1 for b in buckets.values() if len(b) > 1)}")
    
    print("\n- Position-weighted (better):")
    buckets = {}
    for word in words:
        h = position_weighted_hash(word, table_size)
        buckets.setdefault(h, []).append(word)
        print(f"  '{word}' -> {h}")
    print(f"  Collisions: {sum(1 for b in buckets.values() if len(b) > 1)}")
