# Find minimum in a list
numbers = [15, 42, 8, 99, 23]
min_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num

print("Minimum:", min_num)
