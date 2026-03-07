# 24_simple_counter.py - Simple class: Counter (mutable state)
# Florentino Baez - ITSE-1002

class Counter:
    """Class with mutable state and methods."""
    def __init__(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def __str__(self):
        return str(self.value)

# Usage
c = Counter(10)
print(f"Start: {c}")
c.increment()
c.increment()
print(f"After +2: {c}")
c.decrement()
print(f"After -1: {c}")
