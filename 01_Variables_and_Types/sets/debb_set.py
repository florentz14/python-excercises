#DEBUGGING EXCERCISES:
# Daniel and Florentino

students = {"Alice", "Bob", "Carlos"}
print("Original set:", students)
print("-" * 40)

# add a new student
# we change append by add to avoid error if the student is already in the set.
students.add("Diana")
print("Added set:", students)
print("-" * 40)

# remove a student
# change remove by discard to avoid error if the student is not in the set.
students.discard("Miguel")
print("Discarded set:", students)
print("-" * 40)
