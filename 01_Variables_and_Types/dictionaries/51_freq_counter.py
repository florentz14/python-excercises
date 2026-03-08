# -------------------------------------------------
# File Name: 51_freq_counter.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Frequency counting: manual loop, get(), setdefault(), Counter.
# -------------------------------------------------

from collections import Counter
text = "hello world hello python world hello"
words = text.split()

# Manual frequency count
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Manual frequency count:", frequency)

# Using get() method
frequency_get = {}
for word in words:
    frequency_get[word] = frequency_get.get(word, 0) + 1

print("Using get():", frequency_get)

# Using setdefault()
frequency_setdefault = {}
for word in words:
    frequency_setdefault.setdefault(word, 0)
    frequency_setdefault[word] += 1

print("Using setdefault:", frequency_setdefault)

# Comparison with collections.Counter
counter_freq = Counter(words)
print("Using Counter:", dict(counter_freq))

# Most common word
most_common = max(frequency.items(), key=lambda x: x[1])
print(f"Most common word: {most_common[0]} ({most_common[1]} times)")
