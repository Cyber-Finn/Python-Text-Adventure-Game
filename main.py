from Scenes.Dungeon.Scene_one import dungeon_intro

# We'll be adding more scenes and choices as we build onto the game,
# but leaving as-is for now, while I build up all the scenes, quests and items, etc.

if __name__ == "__main__":
    # Initialize the game
    print("Welcome to the Adventure Game!")
    print("...")
    player_name = input("Enter your name: ")
    print(f"Good luck, {player_name}!")
    dungeon_intro.dungeon_intro_scene()
