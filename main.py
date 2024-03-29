#this line just ensures that python will see where our game package is (and allow us to reference modules within the package), 
#without us having to edit the pythonPath environment variable
import sys
sys.path.append("C:/Users/Steph/source/repos/Python/Text_Adventure_Game") #todo: replace this to where-ever your version of the project will be located


from Modules.Scenes.Dungeon.Scene_one import dungeon_intro

# We'll be adding more scenes and choices as we build onto the game,
# but leaving as-is for now, while I build up all the scenes, quests and items, etc.

if __name__ == "__main__":
    # Initialize the game
    print("Welcome to the Adventure Game!")
    print("...")
    player_name = input("Enter your name: ")
    print(f"Good luck, {player_name}!")
    dungeon_intro.dungeon_intro_scene()
