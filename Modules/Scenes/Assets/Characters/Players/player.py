class Player:
    def __init__(self, race, name, playerclass, weight, maxweight, inventory, playerStats):
        self.race = race
        self.name = name
        self.playerclass = playerclass
        self.playerStats = playerStats
        self.weight = weight
        self.maxweight = maxweight
        self.inventory = inventory