#we'll eventually just import every NPC file in the directory through a single import, but that'll require modifying the __init__.py
from . import raynor_of_londor
import random

'''

# Holds all respective NPCs
unique_npc_loot_table = [{"item": raynor_of_londor.RaynorOfLondor.npcObject.name, "weight": 1}] # not to be used in "get random npc" methods
monster_npc_loot_table = []
generic_npc_loot_table = []


def get_random_npc(object_name): #this method of dynamically getting the "loot table to search through"'s name, allows us to reuse this code, without having lots of copies of it for each item type (like pendants, swords, etc.)
    # Create a list of items based on their weights
    choices = []
    for entry in object_name:
        item, weight = entry["item"], entry["weight"]
        choices.extend([item] * weight) # expands the choices list by adding multiple copies of the same item according to its specified weight. Items with higher weights have a proportionally greater chance of being selected

    # Select a random item from that expanded list
    selected_item = random.choice(choices)
    return selected_item #cast_object_as_npc(get_object_for_cast(selected_item, object_name))

#might not need these
def get_object_for_cast(itemName, object_name):
    itemObject = get_object(itemName, object_name)
    return itemObject

def get_object(item, object_name):
    if item in object_name:
        return object_name[item]
    else:
        return None

def cast_object_as_npc(itemObject):
    return NPC(
        itemObject.race,
        itemObject.name,
        itemObject.playerclass,
        itemObject.playerStats,
        itemObject.weight,
        itemObject.maxweight,
        itemObject.inventory
        )

'''