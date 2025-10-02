# coke.py
# Simulates a vending machine where the user inserts coins until 50 cents is paid.

amount_due = 50   # total cost

while amount_due > 0:
    paid = int(input("Insert Coins: "))   # user inserts a coin
    
    # accept only 25¢, 10¢, or 5¢
    if paid == 25 or paid == 10 or paid == 5:
        amount_due -= paid
        if amount_due > 0:          # still owe money
            print("Amount Due:", amount_due)
        elif amount_due == 0:       # paid exact
            print("Change owed: 0")
        else:                       # overpaid
            print("Change owed:", abs(amount_due))
    else:
        # reject invalid coin, show same amount due
        print("Amount Due:", amount_due)
        continue
