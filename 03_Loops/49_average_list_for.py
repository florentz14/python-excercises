# Average of numbers
numbers = [85, 90, 78, 92, 88]
total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)
print(f"Average: {average}")
