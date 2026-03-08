# -------------------------------------------------
# File Name: 07_alphabet_remove_multiple_3.py
# Description: Alphabet, remove letters at positions multiple of 3
# -------------------------------------------------

import string
alphabet = list(string.ascii_lowercase)
result = [c for i, c in enumerate(alphabet) if (i + 1) % 3 != 0]
print(result)
