# PART 1 - EXPONENTS
base = int(input("Enter integer as base value: "))
exponent = int(input("enter integer as exponent: "))
result = base ** exponent # example, (3 ** 2) is 3 squared
print(f"{base}  to the {exponent} power is {result} !!")

# PART 2 - ADDITION SUBTRACTION 
print("-----Addition and Subtraction-----")
print("\n") # 2 newlines 
# 3 numbers, start, add this, sub this
start = int(input("Enter the starting integer: "))
print("you typed", start)
add_this = int(input("Enter Integer to add: "))
sub_this = int(input("Enter integer to subtract: "))

answer = start + add_this - sub_this
print()
print() # that gives 2 newlines, so would print("\n")
print(start, "+", add_this, "-", sub_this, "Is equal to", answer)
print(f"{start} + {add_this} - {sub_this} is equal to {answer}")

# John Bardaji
# 9/9/2026
# P1HW2
# A travel expenses calculator 

#  Ask user to enter their budget
Budget = float(input("Enter Budget", ))

# Ask user to enter travel destination
Destination = (input("Enter the travel destination"))

#  Ask user for amount they will spend on gas
Gas = float(input("Enter Gas cost"))

# Ask user for amount they will spend on accommodation
Accomidation = float(input("accomodation "))

