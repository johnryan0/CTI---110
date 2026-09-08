# CTI 110
# P1HW1 - Math
# Bardaji, J
# Do some math processing 


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