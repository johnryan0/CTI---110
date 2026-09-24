# CTI 110
# P3LAB - making change
# Bardaji
# 9/24/26

"""
# Example 1 -- with potions
hp = int(input("How many hit points of damage (1-100):"))
print("you took ", hp, "Damage!")

# Large potions heal 25
large = hp // 25         # each potion heals 25
hp    = hp % 25          # some damage left over

print("Drank ", large, "large potions.")
print("Damage remaining: ", hp)

# Small potions heal 5
small = hp // 5
hp    = hp % 5

print("Drank", small, "small potions.")
print("Damage remaining: ", hp)
"""


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