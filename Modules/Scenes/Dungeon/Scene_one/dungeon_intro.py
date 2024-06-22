# Imports
from .Loot_controller import controller
from ...Assets.Items.Magic.Wearables.Small import magic_pendants
from ....Utils.Player_Inventory import inventory_system

# The opening/entry scene 
def dungeon_intro_scene():
    print("\nYou find yourself standing at the entrance of a narrow, damp tunnel.")
    print("The flickering torches on the walls cast eerie shadows around you.")
    print("Your heart races as you step forward, uncertain of what lies ahead.")
    print("Choose your next move:")
    print("1. Proceed deeper into the tunnel.")
    print("2. Turn back and exit the tunnel.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        deeperIntoTunnel()
    elif choice == "2":
        exitTunnel()
    else:
        print("Invalid choice. Try again.")
        dungeon_intro_scene() # repeat our intro scene if their choice was invalid

def exitTunnel(): # todo: beef this one up and pass control to the forest scene
    print("Common sense prevails! You turn and run as fast as you can.")
    print("After what feels like an eon, you find yourself standing in a forest clearing.")


# The player ventures deeper into the tunnel.
def deeperIntoTunnel():
    print("\nYou continue cautiously, the darkness enveloping you.")
    print("Suddenly, you hear footsteps echoing from behind.")
    print("Do you:")
    print("1. Hide in the shadows.")
    print("2. Confront the approaching figure.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        hideInShadows()
    elif choice == "2":
        confrontFigure()
    else:
        print("Invalid choice. Try again.")
        deeperIntoTunnel()

# The player hides in the shadows.
def hideInShadows():
    print("\nYou press yourself against the cold stone wall, heart pounding.")
    print("The figure passes by, cloaked in darkness.")
    print("As they disappear, you notice a glimmering pendant on the ground.")
    print("Do you pick it up?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        # in this sub-scene, we specifically want only a pendant (this programming-approach, on the next line, gives us more control over the types of items the player will get/encounter at this point)
        item = controller.get_random_item_pendant(controller.loot_table_pendants) 
        # this next line makes the game more modular by dynamically/procedurally getting items and their "interaction descriptions", instead of having it all hardcoded all over the place!
        print(f"{magic_pendants.get_interaction_description(item)}") 
        inventory_system.add_to_inventory(item)
        #inventory_system.list_inventory_items() #just had this line to debug the add_to_inventory functionality
    elif choice == "2":
        continueHiding()
    else:
        print("Invalid choice. Try again.")
        hideInShadows() #repeat the sub-scene

# The player remains hidden.
def continueHiding():
    print("\nYou stay hidden, heart still racing.")
    print("The footsteps fade away, and you decide to keep moving.")
    # todo: add more 

# The player confronts the approaching figure.
def confrontFigure():
    print("\nYou step forward, ready to face the unknown figure.")
    print("The figure turns — a hooded woman with piercing blue eyes.")
    print("She introduces herself as Erin of Londor, a lost cleric of the House of Londor.") #can abstract this into a file for different NPCs in future, like we did for the pendants
    # todo: Call the next scene here