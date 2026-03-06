# Debugging Assignment
numbers = (4, 8, 12, 16, 20, 24, 28, 32)
print("Using for loop")
for i in range(len(numbers)):
    #numbers[i] = numbers[i] + 1 # this would change the value of the tuple, but it is not allowed
    print(numbers[i])

print("Using while loop")
i = 0
total = 0
while i < len(numbers): #change the <= to < and it will work
    total = total + numbers[i] # this accumulates the total of the numbers
    i += 1 # this increments the index by 1
print("Total:", total)
#functions worksheet due today
#lab 5 is due today
