from Modules.Scenes.Assets.Items import item_system

# just keeping the last line as a variable up here - for easier code reuse
pendant_last_line = "\r\nYou tuck the pendant into your pocket and move forward."

# actual data for the game object (such as name, weight, etc)
azure_pendant = item_system.Item(name="Azure Pendant", type = "Pendant", description="A delicate silver chain with a blue gemstone ", 
                                 interaction_description=
                                 "You pick up the pendant — a delicate silver chain with a blue gemstone.\
                                 \r\nAs you examine it, a voice whispers in your mind:\r\n\"Seek the Oracle. Only she can guide you.\"\
                                 " + pendant_last_line
                                 , weight = 1) #this is actual weight, will impact Inventory capacity and Movement weight

angel_tear = item_system.Item(name="Angel's Tear", type = "Pendant", description="A beautiful crystalline necklace. You have never seen such purity before.", 
                                 interaction_description=
                                 "You pick up the glimmering necklace — it shimmers in the light.\
                                 \r\nAs you examine it, a strange feeling befalls you.. \
                                 \r\nThis item has been held by Kings and beggars alike, and you will not be its last holder.\
                                 " + pendant_last_line
                                 , weight = 1)

# todo: martry's breathe would make a good weapon upgrade material
# todo: also need to look into status effects or item-effects/abilities
martyr_embrace = item_system.Item(name="Martry's Last Embrace", type = "Pendant", description="A drop of crystallised blood, held in place by threads of intertwining spikes - ready to burrow into flesh",  
                                 interaction_description=
                                 "You pick up the thorny diadem — the single drop of crystallized blood shimmering under examination.\
                                 \r\nSuddenly, a strange feeling befalls you.. \
                                 \r\nHope, regret, pain and emptiness explode in your chest. Then, only emptiness remains..\
                                 " + pendant_last_line
                                 , weight = 1)


# data struct to hold info about my pendants -> just so we can access the items later on from other code files
game_objects = {
    "Azure Pendant": azure_pendant,
    "Angel's Tear": angel_tear,
    "Martry's Last Embrace": martyr_embrace
    
    # Add other objects here...
    #   ensure that the name matches the game object you added at the top (below the import)
}

# todo: can probably abstract this out to a central method/file but leaving as-is for now, until we get the full framework in place [housekeeping item]
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
    
def get_object(object_name):
    if object_name in game_objects:
        return game_objects[object_name]
    else:
        return None