# These are just objects that define what the item types are,
# We have methods for handling the inventory in the: inventory_system .py file within Modules.Utils.Player_Inventory

# items that dont stack -> like swords, heavy objects
class Item:
    def __init__(self, type, name, description, interaction_description, weight):
        self.type = type
        self.name = name
        self.description = description
        self.interaction_description = interaction_description
        self.weight = weight

# items that can stack -> like our potions, etc. (Up to a certain weight limit!)
class StackableItem(Item):
    def __init__(self, type, name, description, interaction_description, weight, max_stack_size=10):
        super().__init__(type, name, description, interaction_description, weight)
        self.max_stack_size = max_stack_size
        self.stack_count = 1