# some NPCs can be multi-instance (like monsters), but support-character NPCs should only exist in one instance (dont want 3x Geralt of Rivias in the world at once, for example)

from . import npc_definition
'''
class RaynorOfLondor:
    def __init__(self, npcObject:npc_definition.NPC.__init__ = npc_definition.NPC( 
                    #loading up some default attribs - in case no object is passed in
                    "Human",
                    "Raynor of Londor",
                    "Cleric",
                    "Temp",
                    "60",
                    "85",
                    list()
                 )): #will have all the same info (like health, etc.) as a player, with some added attribs
        self.npcObject = npcObject

'''