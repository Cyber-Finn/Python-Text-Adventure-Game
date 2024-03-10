from .... import item_system

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
    "azure_pendant": azure_pendant
    # Add other objects here...
}


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