 # john Bardaji

 # 9/20/26

 # P2HW1

 # Travel Expenses calculator with oganized output 

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
print(f"{'Location:':<20} {Destination}")
print(f"{'Initial budget:':<20} ${Budget:,.2f}")
print(f"{'Fuel:':<20} ${Gas:,.2f}")
print(f"{'Accomodation:':<20} ${Accomodation:,.2f}")
print(f"{'Food:':<20} ${Food:,.2f}")
print(f"{'Remaining balance:':<20} ${Results:,.2f}")
print("-----------------------------------")