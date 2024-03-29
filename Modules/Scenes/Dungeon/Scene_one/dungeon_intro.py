
from .Loot_controller import controller
from ...Assets.Items.Magic.Wearables.Small import magic_pendants

#The opening scene 
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
        dungeon_intro_scene() # repeat our intro scene

def exitTunnel(): # todo: beef this one up and pass control to the forest scene
    print("Common sense prevails! You turn and run as fast as you can.")
    print("After what feels like an eon, you find yourself standing in a forest clearing.")


#The player ventures deeper into the tunnel.
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

#The player hides in the shadows.
def hideInShadows():
    print("\nYou press yourself against the cold stone wall, heart pounding.")
    print("The figure passes by, cloaked in darkness.")
    print("As they disappear, you notice a glimmering pendant on the ground.")
    print("Do you pick it up?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        #foundPendant()
        item = controller.get_random_item()
        print(f"{magic_pendants.get_interaction_description(item)}") # this lets us make the game more modular by having us randomly get items and the "interaction descriptions", instead of having it all hardcoded!
    elif choice == "2":
        continueHiding()
    else:
        print("Invalid choice. Try again.")
        hideInShadows()

def foundPendant(): # might abstract this so that all items have these kinds of descriptions, and we can just select a random one - rather than hardcoded
    print("\nYou pick up the pendant—a delicate silver chain with a blue gemstone.")
    print("As you examine it, a voice whispers in your mind:")
    print("\"Seek the Oracle. Only she can guide you.\"")
    print("You tuck the pendant into your pocket and move forward.")
    # Call the next scene here (e.g., encounterErin())

def continueHiding():
    """
    The player remains hidden.
    """
    print("\nYou stay hidden, heart still racing.")
    print("The footsteps fade away, and you decide to keep moving.")
    # Call the next scene here

def confrontFigure():
    """
    The player confronts the approaching figure.
    """
    print("\nYou step forward, ready to face the unknown.")
    print("The figure turns—a hooded woman with piercing blue eyes.")
    print("She introduces herself as Erina, a fellow traveler.")
    print("\"I've been searching for answers,\" Erina says. \"Have you found anything?\"")
    # Call the next scene here

if __name__ == "__main__":
    print("Welcome to the Adventure Game!")
    print("As an avid traveler, you have decided to visit the Catacombs of Paris.")
    print("However, during your exploration, you find yourself lost.")
    print("You can choose to walk in multiple directions to find a way out.")
    name = input("Let's start with your name: ")
    print("Good luck, " + name + ".")
    dungeon_intro_scene()
