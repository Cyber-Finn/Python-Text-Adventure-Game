# Initialize the player's inventory
inventory = []

# Define the healing potion and sword
healing_potion = "Healing Potion"
sword = "Sword"

# Function to add an item to the inventory
def add_to_inventory(item):
    if item not in inventory:
        inventory.append(item)
        print(f"Added {item} to your inventory.")
    else:
        print(f"You already have {item} in your inventory.")