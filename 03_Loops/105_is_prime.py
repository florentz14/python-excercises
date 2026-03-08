# -------------------------------------------------
# File Name: 105_is_prime.py
# Description: Check if number is prime
# -------------------------------------------------

n = int(input("Enter an integer: "))
if n < 2:
    print("Not prime")
else:
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    print("Prime" if prime else "Not prime")
