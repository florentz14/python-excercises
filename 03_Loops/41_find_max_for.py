# Find maximum in a list
numbers = [15, 42, 8, 99, 23]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("Maximum:", max_num)
