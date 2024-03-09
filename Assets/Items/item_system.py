# items that dont stack -> like swords, heavy objects
class Item:
    def __init__(self, type, name, description, weight):
        self.type = type
        self.name = name
        self.description = description
        self.weight = weight

# items that can stack -> like our potions, etc. (Up to a certain weight limit!)
class StackableItem(Item):
    def __init__(self, name, description, weight, max_stack_size=10):
        super().__init__(name, description)
        self.weight = weight
        self.max_stack_size = max_stack_size
        self.stack_count = 1

    