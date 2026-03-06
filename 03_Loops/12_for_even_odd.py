"""For loop: Even/odd classification.
Classifies numbers 1-10 as even or odd using modulo.
"""
# Author: Florentino Báez


for count in range(1, 11):
    if count % 2 == 0:
        print(count, "is even")
    else:
        print(count, "is odd")
