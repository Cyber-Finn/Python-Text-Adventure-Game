import json

# Example game state vars -> will be changing how we get this in here, but leaving as is for now: todo: revisit
player_stats = {"health": 100, "mana": 50}
inventory = ["Sword", "Healing Potion"]
current_scene = "Forest"
quest_progress = {"main_quest": 2, "side_quest": 1}
character_info = {"race": "Human", "looks": "Tall", "stats": {"strength": 8, "agility": 6}}

# Save game state to a JSON file
def save_game_state():
    game_state = {
        "player_stats": player_stats,
        "inventory": inventory,
        "current_scene": current_scene,
        "quest_progress": quest_progress,
        "character_info": character_info
    }
    with open("save_game.json", "w") as save_file: #same as with C/C++ FILE -> "w" is to write, "r" is to read
        json.dump(game_state, save_file, indent=4)

# Load game state from the JSON file
def load_game_state():
    try:
        with open("save_game.json", "r") as save_file:
            loaded_data = json.load(save_file)
            return loaded_data
    except FileNotFoundError:
        print("No saved game found.")
        return None

# Example usage
save_game_state()
loaded_data = load_game_state()
if loaded_data:
    print("Loaded game state:", loaded_data)
