# -------------------------------------------------
# File Name: Baez_Module_02_01_distance.py
# Author: Florentino Báez
# Date: Baez_Module_02_Lab
# Description: Demonstrates baez module 02 01 distance.
# -------------------------------------------------

print("=" * 60)
print("EXERCISE 1: Distance Traveled Program")
print("=" * 60)

SPEED = 70  # miles per hour
TIMES = [6, 10, 15]  # hours

for time in TIMES:
    distance = SPEED * time
    print(
        f"The distance the car will travel in {time} hours: {distance} miles")

print()
