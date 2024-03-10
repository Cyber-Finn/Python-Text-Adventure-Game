import random
from ....Assets.Items.Magic.Wearables.Small import magic_pendants
# Define your loot table (item, weight) pairs
loot_table = [
    {"item": magic_pendants.azure_pendant, "weight": 100}
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
    item_name = next(entry["item"] for entry in loot_table if entry["item"] == selected_item)

    return item_name



# just here for debugging: running into an issue where this package isnt importing the magic_pendants -> even though it finds it perfectly fine..
if __name__ == "__main__":
    print(get_random_item)