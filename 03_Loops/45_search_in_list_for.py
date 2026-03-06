# Check if number exists in list
numbers = [10, 20, 30, 40, 50]
search = 30
found = False

for num in numbers:
    if num == search:
        found = True
        break

if found:
    print(f"{search} is in the list")
else:
    print(f"{search} is not in the list")
