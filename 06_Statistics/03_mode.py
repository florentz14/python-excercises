# -------------------------------------------------
# File Name: 03_mode.py
# Author: Florentino Báez
# Description: Finds the mode (most frequent value) and includes multimode for datasets with multiple modes.
# -------------------------------------------------

import statistics # Statistical functions

data = [12, 15, 18, 22, 25, 25, 28, 30, 33, 40] # Data set

print("=== DATA ===")
print(data) # Data set
print()

# Mode
mode = statistics.mode(data) # Mode
print(f"Mode (most frequent): {mode}") # Mode (most frequent)
print()

# multimode si hay más de una moda (Python 3.8+)
modes = statistics.multimode(data) # Multimode
print(f"multimode: {modes}") # Multimode
