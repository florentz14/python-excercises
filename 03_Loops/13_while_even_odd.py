"""While loop: Even/odd classification.
Classifies numbers 1-10 as even or odd using modulo.
"""
# Author: Florentino Báez


count = 1

while count <= 10:
    if count % 2 == 0:
        print(count, "is even")
    else:
        print(count, "is odd")
    count = count + 1
