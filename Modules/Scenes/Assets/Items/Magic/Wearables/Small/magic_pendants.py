#this line just ensures that python will see where our game package is (and allow us to reference modules within the package), 
#without us having to edit the pythonPath environment variable
import sys
sys.path.append("C:/Users/Steph/source/repos/Python/Text_Adventure_Game") #todo: replace this to where-ever your version of the project will be located



#from .... import item_system
from Modules.Scenes.Assets.Items import item_system

azure_pendant = item_system.Item(name="Azure Pendant", type = "Pendant", description="A delicate silver chain with a blue gemstone ", 
                                 interaction_description=
                                 "You pick up the pendant — a delicate silver chain with a blue gemstone.\
                                 \r\nAs you examine it, a voice whispers in your mind:\r\n\"Seek the Oracle. Only she can guide you.\"\
                                 \r\nYou tuck the pendant into your pocket and move forward."
                                 , weight = 1)

angel_tear = item_system.Item(name="Angel's Tear", type = "Pendant", description="A ranged weapon for precise shots", 
                                 interaction_description=
                                 "You pick up the glimmering necklace — it shimmers in the light.\
                                 \r\nAs you examine it, a strange feeling befalls you.. \
                                 \r\nThis item has been held by Kings and beggars alike, and you will not be its last holder.\
                                 \r\nYou tuck the pendant into your pocket and move forward."
                                 , weight = 1)


# data struct to hold info about my pendants -> just so we can access the items later on
game_objects = {
    "Azure Pendant": azure_pendant,
    "Angel's Tear": angel_tear
    #azure_pendant
    
    # Add other objects here...
}

def debugObjects(object_name):
    if object_name in game_objects:
        return game_objects[object_name].interaction_description


def get_interaction_description(object_name):
    if object_name in game_objects:
        return game_objects[object_name].interaction_description
    else:
        return None
    
def get_description(object_name):
    if object_name in game_objects:
        return game_objects[object_name].description
    else:
        return None
    


if __name__ == "__main__":
    testobj = debugObjects("Azure Pendant")
    print(testobj)