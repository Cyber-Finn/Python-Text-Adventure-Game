# Imports
from .Loot_controller import controller
from ...Assets.Items.Magic.Wearables.Small import magic_pendants
from ....Utils.Player_Inventory import inventory_system


# just using ANSI Escape Codes for changing the terminal/cmd's text colour
class colour:
    blueText = '\033[94m'
    cyanText = '\033[96m'
    greenText = '\033[92m'
    yellowText = '\033[93m'
    FAIL = '\033[91m'
    normalWhiteText = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# White text represents what you as the player choose to do
def printWhiteText(message: list = []):
    for messagestring in message:
        print(colour.normalWhiteText + messagestring)

# Blue text represents world-building or narration
def printBlueText(message: list = []):
    for messagestring in message:
        print(colour.blueText + messagestring)

# Green text represents choices that the narrator has given you
def printGreenText(message: list = []):
    for messagestring in message:
        print(colour.greenText + messagestring)

# Yellow text represents invalid choices or warnings
def printYellowText(message: list = []):
    for messagestring in message:
        print(colour.yellowText + messagestring)

# Cyan text represents items, inventory items or item descriptions
def printCyanText(message: list = []):
    for messagestring in message:
        print(colour.cyanText + messagestring)

#just displays the "choose" message, and lets us get the players input
def getInput(message):
    return input(colour.normalWhiteText + message)

# The opening/entry scene 
def dungeon_intro_scene():
    printBlueText(["\nYou find yourself standing at the entrance of a narrow, damp tunnel.", "The flickering torches on the walls cast eerie shadows around you.", "Your heart races as you step forward, uncertain of what lies ahead."])
    printGreenText(["Choose your next move:", "1. Proceed deeper into the tunnel.", "2. Turn back and exit the tunnel."])
    choice = getInput("Enter 1 or 2: ")

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
    printBlueText(["\nYou continue cautiously, the darkness enveloping you.", "Suddenly, you hear footsteps echoing from behind."])
    printGreenText(["Do you:", "1. Hide in the shadows.", "2. Confront the approaching figure."])

    choice = getInput("Enter 1 or 2: ")

    if choice == "1":
        hideInShadows()
    elif choice == "2":
        confrontFigure()
    else:
        printYellowText(["Invalid choice. Try again."])
        deeperIntoTunnel()

# The player hides in the shadows.
def hideInShadows():
    printBlueText(["\nYou press yourself against the cold stone wall, heart pounding.", "The figure passes by, cloaked in darkness.", "As they disappear, you notice a glimmering pendant on the ground."])
    printGreenText(["Do you pick it up?", "1. Yes", "2. No"])

    choice = getInput("Enter 1 or 2: ")

    if choice == "1":
        # in this sub-scene, we specifically want only a pendant (this programming-approach, on the next line, gives us more control over the types of items the player will get/encounter at this point)
        item = controller.get_random_item_pendant(controller.loot_table_pendants) 
        # this next line makes the game more modular by dynamically/procedurally getting items and their "interaction descriptions", instead of having it all hardcoded all over the place!
        printCyanText([f"{magic_pendants.get_interaction_description(item.name)}"]) 
        inventory_system.add_to_inventory(item)
        #just had these last few lines to debug the add_to_inventory functionality
        #inventory_system.list_inventory_items() 
        #if inventory_system.remove_from_inventory(item.name):
            #inventory_system.list_inventory_items()
    elif choice == "2":
        continueHiding()
    else:
        printYellowText(["Invalid choice. Try again."])
        hideInShadows() #repeat the sub-scene

# The player remains hidden.
def continueHiding():
    printBlueText(["\nYou stay hidden, heart still racing.", "The footsteps fade away, and you decide to keep moving."])
    # todo: add more 

# The player confronts the approaching figure.
def confrontFigure():
    printBlueText(["\nYou step forward, ready to face the unknown figure.", "The figure turns and your eyes fall on a hooded woman with piercing blue eyes.", "She introduces herself as Erin of Londor, a lost cleric of the House of Londor."])
    # todo: Call the next scene here
    #todo: can abstract NPC info into a file for different NPCs in future, like we did for the pendants