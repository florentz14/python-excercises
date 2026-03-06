# -------------------------------------------------
# File Name: 29_nested_loop3.py
# Author: Florentino Báez
# Date: 19/02/2026
# professor: Mauricio Quiroga
# Description: Nested Loop Through a Dictionary of Dictionaries.
#              Shows how to work with dictionaries inside
#              dictionaries. Includes accessing nested values,
#              iterating, modifying, removing items, adding new items...
# -------------------------------------------------

print("Nested Loop Through a Dictionary")
print("-" * 40)

# create a nested dictionary of dictionaries
myFamily = {
    "child1": {
        "name": "Emiliano",
        "year": 2004,
        "weight": 7
    },
    "child2": {
        "name": "Tobias",
        "year": 2007,
        "weight": 6
    },
    "child3": {
        "name": "Pytheas",
        "year": 2011,
        "weight": 9
    }
}

# ---------------------------------------
# UPDATE EXISTING VALUE
# ---------------------------------------
myFamily["child1"]["weight"] = 8

# ---------------------------------------
# REMOVE USING POP()
# ---------------------------------------

# display the nested dictionary of dictionaries
print("Nested Dictionary:", myFamily)
print("-" * 40)

# remove child3 from outer dictionary
removed_child = myFamily.pop("child3")
print(f"\nRemoved child: {removed_child}")
print("-" * 40)

# remove weight from child1
removed_weight = myFamily["child1"].pop("weight")
print(f"\nRemoved weight: {removed_weight}")
print("-" * 40)

# remove year from child1
removed_year = myFamily["child1"].pop("year")
print(f"\nRemoved year: {removed_year}")
print("-" * 40)

# display the nested dictionary of dictionaries
print("Nested Dictionary:", myFamily)
print("-" * 40)

# ---------------------------------------
# ADD NEW CHILD USING update()
# ---------------------------------------

myFamily.update({
    "child4": {
        "name": "Sofia",
        "year": 2025,
        "weight": 6
    }
})

# display the nested dictionary of dictionaries
print("Nested Dictionary:", myFamily)
print("-" * 40)
# ---------------------------------------
# UPDATE INNER DICTIONARY USING update()
# ---------------------------------------

# change year of child2
myFamily["child2"].update({"year": 2008})

# add new key to child1
myFamily["child1"].update({"hair color": "blond"})

print("\nUpdated Dictionary:")
print("-" * 40)
print(myFamily)
print("-" * 40)

# ---------------------------------------
# LOOP THROUGH NESTED DICTIONARY
# ---------------------------------------

for child_label, child_info in myFamily.items():
    print(f"\n{child_label}")
    
    for key, value in child_info.items():
        print(f"\t{key}: {value}")
