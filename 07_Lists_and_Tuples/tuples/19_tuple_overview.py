# ---------------------------------------------------------------------------
# TUPPLE stores multiple items in one single variable
# IS ORDERED AND UNCHANGEABLE
# ---they are indexed starting at 0
# ---unchangeable --> we cannot change, add or remove items
# after the tuple has been created
# ---they can have duplicates
# ---they can have different data types
# ---------------------------------------------------------------------------

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
