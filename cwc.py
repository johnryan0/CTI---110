# CTI 110
# P5LAB - Purchase nd change 
# Bardaji
# Self checkout sim, makes change
import random 

def disperse_change(amount):
    # Print change needed 
    # Input: float
    # Return: nothing
    print(f"Change is: ${amount:.2f}")
    print()
    # put your p3 lab code here

    # example 2 - with coins
amount = float(input("Enter an amount in dollars and cents (ex: 11.56): "))
cents = round(amount * 100)  # convert to cents, round correctly
print("that's", cents, "cents")

    # for each currency type:
# - cents // {currency}
# - cents % {currency} gives you the left over cents
dollars = cents // 100
cents = cents % 100
# If statement - dont show of zero, use singular or plural otherwise 
if dollars == 0:
    pass
if dollars == 1:
    print("1 dollar")
else:
    print(dollars, "dollars")
    
# quarters
quarters = cents // 25
cents = cents % 25
if quarters == 1:
    print("1 quarter")
else:
    print(quarters, "quarters")

# dimes
dimes = cents // 10
cents = cents % 10
if dimes == 1:
    print("1 dime")
else:
    print(dimes, "dimes")

# nickels
nickels = cents // 5
cents = cents % 5
if nickels == 1:
    print("1 nickel")
else:
    print(nickels, "nickels")

# pennies
if cents == 1:
    print("1 penny")
else:
    print(cents, "pennies")

# Main
def main():
    cost = 0.0
    amount_paid = 0.0
    change_owed = 0.0
    print("welcome to the self-checkout sim.")
    cost = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${cost:.2f}")
    amount_paid = float(input("How much money do you put in the self checkout "))
    print("Here is your change:")
    change_owed = amount_paid - cost

    disperse_change(change_owed)



# Last line - start the program
main()
