# CTI 110
# P1HW1 - Math
# Bardaji, J
# Do some math processing 


# PART 1 - EXPONENTS


# PART 2 - ADDITION SUBTRACTION 
# 3 numbers, start, add this, sub this
start = int(input("Enter the starting integer: "))
print("you typed", start)
add_this = int(input("Enter Integer to add: "))
sub_this = int(input("Enter integer to subtract: "))

answer = start + add_this - sub_this
print()
print() # that gives 2 newlines, so would print("\n"
print(start, "+", add_this, "-", sub_this, "Is equal to", answer)
print(f"{start} + {add_this} - {sub_this} is equal to {answer}")