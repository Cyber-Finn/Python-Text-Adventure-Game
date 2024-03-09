class Item:
    def __init__(self, type, name, description):
        self.type = type
        self.name = name
        self.description = description

# Example usage:
sword = Item(name="Sword", type = "Sword", description="A sharp blade for combat")
potion = Item(name="Healing Potion", description="Restores health points")

# example of how to access the properties of an item
print(f"Item: {sword.name}")
print(f"Description: {sword.description}")
