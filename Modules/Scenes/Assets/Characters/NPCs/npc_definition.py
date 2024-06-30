from ..Players import player
# Define what an NPC is
class NPC:
    def __init__(self, playerObject: player.Player): # will have all the same info (like health, etc.) as a player, with some added attribs
        self.playerObject = playerObject