# Initialize the player's inventory
inventory = []

# Function to add an item to the inventory
def add_to_inventory(item):
    if item not in inventory:
        inventory.append(item)
        print(f"Added {item} to your inventory.")
    else:
        print(f"You already have {item} in your inventory.")

# Function to remove an item from the inventory. Returns true if removed, false if not removed (Item didnt exist)
def remove_from_inventory(item_name):
    for item in inventory:
        if item.name.lower() == item_name.lower():
            inventory.remove(item)
            print(f"Removed {item.name} from your inventory.")
            return True

    print(f"{item_name} not found in your inventory.")
    return False