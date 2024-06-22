#Q: what is this file?
#A: this file is our main "controller" logic for all item selection in this scene
#   in this file, we'll load up all the items we want to be able to use in this scene, and their respective probability weights
#   The actual objects are stored in their respective class/object files in the Assets/Items folders.

import random
from Modules.Scenes.Assets.Items.Magic.Wearables.Small  import magic_pendants 
from ....Assets.Items import item_system 

# Define our loot table with (item, weight) pairs
loot_table_pendants = [
    {"item": magic_pendants.azure_pendant.name, "weight": 1}, #weight here is not physical weight, but rather a probability weight (having a high number here will impact resource usage)
    {"item": magic_pendants.angel_tear.name, "weight": 1},
    {"item": magic_pendants.martyr_embrace.name, "weight": 1}
    # todo: add other items and their weights
    # like:
    #   {"item": "Sword", "weight": 30},
    #   {"item": "Potion", "weight": 25},
    #   {"item": "Gold Coin", "weight": 20}
]

loot_table_swords = [
    # todo: add other items and their weights
    # like:
    #   {"item": "Sword", "weight": 30},
    #   {"item": "Potion", "weight": 25},
    #   {"item": "Gold Coin", "weight": 20}
]

def get_random_item_pendant(object_name): #this method of dynamically getting the "loot table to search through"'s name, allows us to reuse this code, without having lots of copies of it for each item type (like pendants, swords, etc.)
    # Create a list of items based on their weights
    choices = []
    for entry in object_name:
        item, weight = entry["item"], entry["weight"]
        choices.extend([item] * weight) # expands the choices list by adding multiple copies of the same item according to its specified weight. Items with higher weights have a proportionally greater chance of being selected

    # Select a random item from that expanded list
    selected_item = random.choice(choices)
    return cast_object_as_item(get_object_for_cast(selected_item, 1))

def get_object_for_cast(itemName, itemType):
    itemObject = any #unsure if this will work
    if itemType == 1:
        itemObject = magic_pendants.get_object(itemName)
    return itemObject

def cast_object_as_item(itemObject):
    return item_system.Item(itemObject.type, itemObject.name, itemObject.description, itemObject.interaction_description, itemObject.weight)