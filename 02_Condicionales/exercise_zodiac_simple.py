# There are 12 animals in the Chinese zodiac, separated by 12 years.

year = int(input("What year were you born? "))

zodiacYear = year % 12  # % is the modulus operator (remainder)

if zodiacYear == 0:  # == means "equal to"
    print("You are a Monkey")
elif zodiacYear == 1:
    print("You are a Rooster")
elif zodiacYear == 2:
    print("You are a Dog")
elif zodiacYear == 3:
    print("You are a Pig")
elif zodiacYear == 4:
    print("You are a Rat")
elif zodiacYear == 5:
    print("You are an Ox")
elif zodiacYear == 6:
    print("You are a Tiger")
elif zodiacYear == 7:
    print("You are a Rabbit")
elif zodiacYear == 8:
    print("You are a Dragon")
elif zodiacYear == 9:
    print("You are a Snake")
elif zodiacYear == 10:
    print("You are a Horse")
elif zodiacYear == 11:
    print("You are a Goat")
else:
    print("Something went wrong.")
