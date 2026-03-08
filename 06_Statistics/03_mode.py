# -------------------------------------------------
# File Name: 03_mode.py
# Author: Florentino Báez
# Description: Finds the mode (most frequent value) and includes multimode for datasets with multiple modes.
# -------------------------------------------------

import statistics

data = [12, 15, 18, 22, 25, 25, 28, 30, 33, 40]

print("=== DATA ===")
print(data)
print()

# Mode
mode = statistics.mode(data)
print(f"Mode (most frequent): {mode}")
print()

# multimode si hay más de una moda (Python 3.8+)
modes = statistics.multimode(data)
print(f"multimode: {modes}")
