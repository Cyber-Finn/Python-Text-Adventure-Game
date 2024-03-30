#Q: what is this file?
#A: this file is our main "controller" logic for all item selection
#   in this file, we'll load up all the items we want to be able to use in the game, and their respective probability wieghts
#   the actual objects are stored in their respective class files. We do this, to enable us to add items to the game's code, but not to the game just yet. (Secret/debug items, etc.)

import random
from Modules.Scenes.Assets.Items.Magic.Wearables.Small  import magic_pendants  


#from .....Scenes.Assets.Items.Magic.Wearables.Small  import magic_pendants  
# Define your loot table (item, weight) pairs
loot_table_pendants = [
    {"item": magic_pendants.azure_pendant.name, "weight": 50}, #weight here is not physical weight, but probability weight
    {"item": magic_pendants.angel_tear.name, "weight": 50},
    {"item": magic_pendants.martyr_embrace.name, "weight": 50}
    #{"item": "Sword", "weight": 30},
    #{"item": "Potion", "weight": 25},
    #{"item": "Gold Coin", "weight": 20}
    # todo: add other items and their weights
]

loot_table_swords = [
    # todo: add other items and their weights
]

def get_random_item_pendant(object_name): #this method of dynamically getting the "loot table to search through"'s name, allows us to reuse this code, without having 10 billion copies of it and making the code file massive
    # Create a list of items based on their weights
    choices = []
    for entry in object_name:
        item, weight = entry["item"], entry["weight"]
        choices.extend([item] * weight) # expands the choices list by adding multiple copies of the same item according to its specified weight. ensures that items with higher weights have a proportionally greater chance of being selected

    # Select a random item from that list
    selected_item = random.choice(choices)
    return selected_item