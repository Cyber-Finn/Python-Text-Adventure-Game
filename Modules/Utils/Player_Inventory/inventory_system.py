#from ...Scenes.Assets.Items import item_system

# Initialize the player's inventory
inventory = []
# Initialize the player's max weight (will make this change based on player details)
max_weight = 25 # I'm just assuming 25kg is the total max the average human can carry throughout the day (items on you, etc.)
# just doing this up here for code reusability, and so that we dont clutter the code
too_heavy_message = "A magic back would help right about now! Can't carry any more!"

# Function to add an item to the inventory
def add_to_inventory(item):
    if not_overweight:
        if item not in inventory:
            inventory.append(item)
            print(f"[Game: Added {item.name} to your inventory]")
        else:
            print(f"[Game: You already have {item.name} in your inventory]")
    else:
        print(too_heavy_message)

# Function to remove an item from the inventory. Returns true if removed, false if not removed (Item didnt exist)
def remove_from_inventory(item_name):
    for item in inventory:
        if item.name.lower() == item_name.lower():
            inventory.remove(item)
            print(f"[Game: Removed {item.name} from your inventory]")
            return True

    print(f"[Game: {item_name} not found in your inventory]")
    return False


# methods for adding stackable items to inventory (for stuff like potions, money, etc.)
def add_to_stack(self):
        if not_overweight:
            if self.stack_count < self.max_stack_size:
                self.stack_count += 1
                print(f"[Game: Added {self.name} to your stack (total items: {self.stack_count})]")
            else:
                print(f"[Game: Your {self.name} stack is already full]")
                #should probably just create a new stack in this case -> todo: revisit later
        else:
            print(too_heavy_message)

def remove_from_stack(self):
        if self.stack_count > 0:
            self.stack_count -= 1
            print(f"[Game: Removed {self.name} from your stack (remaining: {self.stack_count})]")
        else:
            print(f"[Game: Your {self.name} stack is empty]")
# end of methods for adding stackable items to inventory 
            
def not_overweight():
    total_weight = 0
    for item in inventory:
        total_weight += sum(item.weight) # dont really need to use sum here, but I like doing this
        if item.stack_count > 1: #if we have a stack (remember that there are 2 item types)
            total_weight += sum(item.weight * sum(item.stack_count-1)) #-1 here, because we've already taken 1 item into account in the line above this IF
    if total_weight >= max_weight:
        return False # they are overweight
    return True # they are fine to carry more

def list_inventory_items():
    if len(inventory) > 0:
        for item in inventory:
            if hasattr(item, 'stack_count'):
                print(f"[Game: Item: {item.name}. Number of items in stack: {item.stack_count}]")
            else:
                print(f"[Game: Item: {item.name}]")
    else:
        print("[Game: You do not have items in your inventory]")
        