# Your Name
# Date
# M3BONUS - Let's Make a Deal
# A short text adventure. The player picks a door and wins a prize.


def calculate_buzzer_pay(seconds_held, dollars_per_second):
    """Return the total pay for holding the buzzer."""
    base_pay = min(seconds_held, 40) * dollars_per_second

    if seconds_held > 40:
        bonus_seconds = seconds_held - 40
        bonus_pay = bonus_seconds * dollars_per_second * 1.5
    else:
        bonus_pay = 0

    total_pay = base_pay + bonus_pay
    return total_pay


def buzzer_round():
    print()
    print("The host smiles. 'Time for the Buzzer Round.'")
    print()
    print("Hold the buzzer as long as you can.")
    print("The first 40 seconds pay the base rate.")
    print("Every second over 40 pays 1.5 times the base rate.")

    seconds_held = float(input("How many seconds did you hold the buzzer? "))
    dollars_per_second = float(input("Dollars per second: "))

    bonus_seconds = max(seconds_held - 40, 0)
    base_pay = min(seconds_held, 40) * dollars_per_second
    bonus_pay = bonus_seconds * dollars_per_second * 1.5
    total_pay = calculate_buzzer_pay(seconds_held, dollars_per_second)

    print()
    print("------------ PRIZE RECEIPT ------------")
    print(f"{'Prize:':<20}Briefcase")
    print(f"{'Seconds held:':<20}{seconds_held:.2f}")
    print(f"{'Bonus seconds:':<20}{bonus_seconds:.2f}")
    print(f"{'Base pay:':<20}${base_pay:.2f}")
    print(f"{'Bonus pay:':<20}${bonus_pay:.2f}")
    print(f"{'Total winnings:':<20}${total_pay:.2f}")
    print("---------------------------------------")


def door_1():
    print()
    print("Door 1 swings open.")
    print("A goat looks at you. It is chewing your ticket.")
    print("You win: one goat.")
    print("The host offers you a second chance.")


def door_2():
    print()
    print("Door 2 swings open.")
    print("Lights flash. A small red car rolls out.")
    print("You win: a car.")
    print("The host gestures toward a bonus chamber.")


def door_3():
    print()
    print("Door 3 swings open.")
    print("A briefcase sits on a stool.")
    print("You win: the briefcase.")
    buzzer_round()


def treasure_room():
    print()
    print("You step into the Treasure Room.")
    print("A golden coin glows in the center of the room.")
    print("You collect the coin and continue the game.")


def ending_room():
    print()
    print("You reach the final chamber.")
    print("The host smiles and says: 'You solved the deal.'")
    print("You win the grand prize: an unforgettable story!")


def start():
    print("=" * 40)
    print("     WELCOME TO LET'S MAKE A DEAL")
    print("=" * 40)
    print("Choose a room to explore:")
    print("1. Goat Room")
    print("2. Car Room")
    print("3. Briefcase Room")
    print("4. Treasure Room")
    print("5. Final Chamber")

    choice = input("Pick a room number (1-5): ")

    if choice == "1":
        door_1()
    elif choice == "2":
        door_2()
    elif choice == "3":
        door_3()
    elif choice == "4":
        treasure_room()
    elif choice == "5":
        ending_room()
    else:
        print("The host frowns. That is not a valid room.")


if __name__ == "__main__":
    start()
