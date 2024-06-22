#this next line just ensures that python will see where our game package is (and allow us to reference modules within the package), 
#without us having to edit the pythonPath environment variable
import sys
sys.path.append("C:/Users/Text_Adventure_Game") #todo: replace this with wherever your version of the project will be located
from Modules.Scenes.Dungeon.Scene_one import dungeon_intro

player_name = "" # global variable for the player's name (todo: Can save this to a file later and read from it when the player has saved)

# We'll be adding more scenes and choices as we build onto the game,
# but leaving the starting scene as-is for now, while I build up all the other scenes, quests and items, etc.

if __name__ == "__main__":
    # Initialize the game
    print("Welcome to the Adventure Game!")
    print("...")
    player_name = input("Enter your name: ")
    print(f"Good luck, {player_name}!")
    dungeon_intro.dungeon_intro_scene()
