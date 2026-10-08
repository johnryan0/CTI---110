# John Bardaji
# P4LAB2
# 10/8/2026


# warmup
"""
for number in (1,2,3,4):
    print(number)
for number in range(5):
    print(number)
for beer in range(99, 0, -1):
    print(beer ,"bottles of beer on the wall")


for mult in range(1,, 13):
    print (7 * mult)

"""

# set up variables 
# start the main loop 
again = "yes"
while again == "yes":
    # Ask the user for their chosen integer (0-12)
    multiplier = int(input("Enter a number 1-12: "))
    # validate (loop)
    while multiplier < 0 or multiplier > 12:
        print("That is not a valid number.")
        multiplier = int(input("Enter a number 1-12: "))



    # print the times table header 
    print("Multiplcation Table")
    print("-"*20)
    # # print the times table (loop)
    for number in range(1, 13):
        print(f"{multiplier} * {number} = {number * multiplier}" )
    # ask if they want to repeat
    again = input("Run again? (yes/no) ")

# outside loop
print()
print("Exiting program... ")