total = 0

data = int(input("Enter a number (0 to exit): "))

while data != 0:
    total = total + data
    data = int(input("Enter a number (0 to exit): "))

print("The total sum is:", total)
