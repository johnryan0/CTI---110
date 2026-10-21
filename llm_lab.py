# Minecraft Smelting Calculator

# How many items each fuel source can smelt
FUEL_VALUES = {
    "coal": 8,
    "charcoal": 8,
    "coal block": 80,
    "lava bucket": 100,
    "blaze rod": 12,
    "dried kelp block": 20,
    "bamboo": 0.25,
    "stick": 0.5,
    "wooden planks": 1.5,
}

def main():
    print("=== Minecraft Smelting Calculator ===")

    item = input("Enter the item you want to smelt: ").strip()
    
    try:
        amount = int(input("Enter the amount of items: "))
        if amount <= 0:
            print("Please enter an amount greater than 0.")
            return
    except ValueError:
        print("Please enter a valid whole number.")
        return

    print("\nChoose your fuel:")
    for fuel, value in FUEL_VALUES.items():
        print(f"- {fuel.title()}: smelts {value:g} items")

    fuel = input("\nEnter your fuel type: ").strip().lower()

    if fuel not in FUEL_VALUES:
        print("Unknown fuel type.")
        return

    # Calculate fuel needed
    smelts_per_fuel = FUEL_VALUES[fuel]
    fuel_needed = int(-(-amount // smelts_per_fuel))

    # Standard furnace processes one item every 10 seconds
    smelting_time = amount * 10

    print("\n=== Results ===")
    print(f"Item: {item}")
    print(f"Items to smelt: {amount}")
    print(f"Fuel: {fuel.title()}")
    print(f"Fuel items needed: {fuel_needed}")
    print(f"Smelting time in one furnace: {smelting_time} seconds")
    print(f"Smelting time in minutes: {smelting_time / 60:.1f} minutes")

    # Calculate furnaces needed to process everything in parallel
    furnaces = (amount + 63) // 64
    print(f"Furnaces to process 64 items each: {furnaces}")

if __name__ == "__main__":
    main()