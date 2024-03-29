import random

#this line just ensures that python will see where our game package is (and allow us to reference modules within the package), 
#without us having to edit the pythonPath environment variable
import sys
sys.path.append("C:/Users/Steph/source/repos/Python/Text_Adventure_Game") #todo: replace this to where-ever your version of the project will be located

from Modules.Scenes.Assets.Items.Magic.Wearables.Small  import magic_pendants  


#from .....Scenes.Assets.Items.Magic.Wearables.Small  import magic_pendants  
# Define your loot table (item, weight) pairs
loot_table = [
    {"item": magic_pendants.azure_pendant.name, "weight": 50}, #weight here is not physical weight, but probability weight
    {"item": magic_pendants.angel_tear.name, "weight":50}
    #{"item": "Sword", "weight": 30},
    #{"item": "Potion", "weight": 25},
    #{"item": "Gold Coin", "weight": 20}
    # todo: add other items and their weights
]

def get_random_item():
    # Create a list of items based on their weights
    choices = []
    for entry in loot_table:
        item, weight = entry["item"], entry["weight"]
        choices.extend([item] * weight) # expands the choices list by adding multiple copies of the same item according to its specified weight. ensures that items with higher weights have a proportionally greater chance of being selected

    # Select a random item from that list
    selected_item = random.choice(choices)

    # Retrieve the name of the selected item
    #item_name = next(entry["item"] for entry in loot_table if entry["item"] == selected_item)

    return selected_item



# just here for debugging: running into an issue where this package isnt importing the magic_pendants -> even though it finds it perfectly fine..
if __name__ == "__main__":
    print(get_random_item)