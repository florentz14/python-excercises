# strings/ - String algorithms and exercises

Programs related to string manipulation and algorithms.

## Structure

| # | File                                     | Description                          |
|---|------------------------------------------|--------------------------------------|
| 01 | `01_valid_palindrome.py`                 | Check if string is a valid palindrome |
| 02 | `02_longest_unique_substring_bruteforce.py` | Longest substring without repeating (brute force) |
| 03 | `03_longest_unique_substring_sliding_window.py` | Longest substring (sliding window) |
| 04 | `04_longest_unique_substring_dict.py`   | Longest substring (dict, jump left)  |
| 05 | `05_longest_unique_substring_freq_counter.py` | Longest substring (defaultdict freq) |

## Files

### `01_valid_palindrome.py` - Valid Palindrome

**What it does:** Checks whether a string is a palindrome. Ignores spaces,
punctuation, and symbols. Case-insensitive.

**Example:** `"A man, a plan, a canal: Panama"` → `true`

**Complexity:** O(n) time, O(1) space (two pointers).

### `02_longest_unique_substring_bruteforce.py` - Brute force

For each starting position, expand right until a repeated character. **O(n²) time, O(n) space.**

### `03_longest_unique_substring_sliding_window.py` - Sliding window

Two pointers (left, right) and a set. Shrink window when duplicate found. **O(n) time, O(n) space.**

### `04_longest_unique_substring_dict.py` - Dictionary (recommended)

Store last-seen index per character. Jump left in one step when duplicate found. **O(n) time, O(n) space.**

### `05_longest_unique_substring_freq_counter.py` - Frequency counter

Sliding window with `defaultdict(int)`. Shrink from left when `counter[char] > 1`. **O(n) time, O(n) space.**

## How to run

```bash
cd 01_Variables_and_Types/strings
python 01_valid_palindrome.py
```
