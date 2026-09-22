# CTI 110
# P3T1 warmup with if statements
# Bardaji
# 9/22/26

# main this is the program starting point
def main():
    print("Hello and welcome to the dungeon")
    level = int(input("What level are you? "))
    if level >= 21:
        print("You can enter the dragon's spire dungeon.")
    else:
        print("Try leveling up first")

# Part two, list your potions 
    print("Time to enter the dungeon.")
    potions = int(input("How many health potions did you bring? "))
    if potions == 0:
        print(f"it's dangerous to go alone wihtout potions ")
    elif potions == 1:
        print(f"You have {potions} health potion.")
    elif potions >= 1: 
        print(f"You have {potions} health potions.")
    else:
        print(f"You have {potions}??? how")


    # part 3 boss battle
    print("You are facing the DELUXE OGRE MAGE")
    print("This will be a hard fight")
    if level >= 25:
       if potions > 3:
         print("It takes three potions to get him to low health!")
         print("*** YOU WIN ***")
       else:
           print("You run out of healing before he's weakened")
           print("*** GAME OVER ***")
    else: 
        print("You were not strong enough")
        print("*** GAME OVER ***")

#at the bottom start the program 
main()