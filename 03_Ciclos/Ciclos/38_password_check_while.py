# While loop with break
password = "secret"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")
    attempts = attempts + 1
    
    if user_input == password:
        print("Access granted!")
        break
    else:
        print("Wrong password")

if attempts == max_attempts:
    print("Too many attempts. Access denied.")
