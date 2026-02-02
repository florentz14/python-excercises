# Baez Module 02 - Exercise 1: Distance Traveled
# Author: Florentino Báez

# EXERCISE 1: Distance Traveled Program
# A car is traveling at 70 miles per hour. Display the distance
# the car will travel in 6, 10, and 15 hours.

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
