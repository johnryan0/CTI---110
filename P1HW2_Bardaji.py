
# John Bardaji
# 9/9/2026
# P1HW2
# A travel expenses calculator 

#  Ask user to enter their budget
Budget = int(input("Enter Budget: ", ))

# Ask user to enter travel destination
Destination = (input("Enter your travel destination: "))

#  Ask user for amount they will spend on gas
Gas = int(input("How much do you think you will spend on gas? "))

# Ask user for amount they will spend on accommodation
Accomodation = int(input("Approximetely, how much will you need for Accomodation/hotel? "))

# Ask user for amount they will spend on food
Food = int(input("Last, how much will you spend on Food? "))

# Process user input
Expenses = Gas + Accomodation + Food 
Results = Budget - Expenses

# Show processed input
print("----------Travel Expenses----------")
print("Location:", Destination)
print("Initial budget:", Budget)
print()
print("Fuel:", Gas)
print("Accomodation:", Accomodation)
print("Food:", Food)
print()
print("Remaining balance:", Results)