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

    
# need methods for now actually adding specific items and calling the inventory_system
# likely going to do this based on the "type" of item