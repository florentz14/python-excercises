# -------------------------------------------------
# File Name: 51_counter.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Counter class with mutable state, increment/decrement.
# -------------------------------------------------

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
