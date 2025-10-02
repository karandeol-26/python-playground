# bank.py
# Determines a payout based on how the user greets.

greeting = input("Greeting: ")
greeting = greeting.strip().lower()   # remove spaces + make lowercase

if greeting == "hello" or greeting[0:5] == "hello":   # starts with "hello"
    print("$0")
elif greeting[0] == "h":   # starts with "h"
    print("$20")
else:   # anything else
    print("$100")
