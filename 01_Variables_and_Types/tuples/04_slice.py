# -------------------------------------------------
# File Name: 04_slice.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Slice a Tuple.
# -------------------------------------------------

print("Example 4: Slice a tuple")
print("-" * 40)

letters = ("a", "b", "c", "d", "e", "f")
print("Original tuple:", letters)

print("First 3 elements:", letters[0:3])       # ('a', 'b', 'c')
print("Elements from index 2 to 4:", letters[2:5])  # ('c', 'd', 'e')
print("Every second element:", letters[::2])   # ('a', 'c', 'e') — step of 2

nums = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print("\nOriginal tuple:", nums)

# Basic [start:stop]
print("\n--- Basic [start:stop] ---")
print("nums[:] (full copy):", nums[:])
print("nums[0:3] (first 3):", nums[0:3])
print("nums[:3] (first 3):", nums[:3])
print("nums[3:] (from index 3):", nums[3:])
print("nums[2:5] (indices 2 to 4):", nums[2:5])
print("nums[5:] (from index 5):", nums[5:])
print("nums[:5] (up to index 5):", nums[:5])
print("nums[2:] (from index 2):", nums[2:])

# Negative indices
print("\n--- Negative indices ---")
print("nums[-3:] (last 3):", nums[-3:])
print("nums[:-2] (all except last 2):", nums[:-2])
print("nums[-5:-2] (5th to 2nd from end):", nums[-5:-2])

# With step [start:stop:step]
print("\n--- With step ---")
print("nums[::2] (every 2nd element):", nums[::2])
print("nums[::3] (every 3rd element):", nums[::3])
print("nums[1::2] (every 2nd from index 1):", nums[1::2])
print("nums[2:8:2] (indices 2-7, every 2nd):", nums[2:8:2])

# Reverse
print("\n--- Reverse ---")
print("nums[::-1] (reverse):", nums[::-1]) # (100, 90, 80, 70, 60, 50, 40, 30, 20, 10)
print("nums[::-2] (reverse every 2nd):", nums[::-2]) # (100, 80, 60, 40, 20)
print("nums[8:2:-1] (index 8 to 3 in reverse):", nums[8:2:-1]) # (90, 80, 70, 60, 50, 40, 30, 20, 10)

# Slicing on strings
print("\n--- Slicing on string word ---")
word = "Hello, World!"
print("Original word:", word) # 'Hello, World!'
print("Copy of word:", word[:]) # 'Hello, World!'
print("word[1:4]:", word[1:4]) # 'ell'
print("word[1:4:2]:", word[1:4:2]) # 'el' -> 'el'
print("word[::-1]:", word[::-1]) # '!dlroW ,olleH' -> '!dlroW ,olleH'

# Slicing on strings
print("\n--- Slicing on string word2 ---")
word2 = "Python"
print("Original word2:", word2) # 'Python'
print("Copy of word2:", word2[:]) # 'Python'
print("word2[1:4]:", word2[1:4]) # 'yth'
print("word2[1:4:2]:", word2[1:4:2]) # 'yh'
print("word2[::-1]:", word2[::-1]) # 'nohtyP' -> 'nohtyP'



