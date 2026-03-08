# -------------------------------------------------
# File Name: 19_tuple_overview.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Demonstrates tuple overview.
# -------------------------------------------------

myFirstTuple = ("London", "Ankara", "Köln", 1945)

print(myFirstTuple)
print(len(myFirstTuple))

# access items in a Tuple
print(myFirstTuple[1])

# access the last item in the Tuple
print(myFirstTuple[-1])

# check if there is an item
if "Köln" in myFirstTuple:
    print("yes, Köln is in your tuple")

# change the Tuple???? WE CANNOT CHANGE A TUPLE
# It is unchangeable or immutable
# you can add a tuple to another tuple
anotherCity = ("Bodrum",)
myFirstTuple += anotherCity

print(myFirstTuple)

# remove items from a tuple YOU CANNOT DO THAT
# BUT, you can delete the tuple completely
del anotherCity
