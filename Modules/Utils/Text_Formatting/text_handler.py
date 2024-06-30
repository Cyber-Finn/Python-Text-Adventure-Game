# just using ANSI Escape Codes for changing the terminal/cmd's text colour
class colour:
    blueText = '\033[94m'
    cyanText = '\033[96m'
    greenText = '\033[92m'
    yellowText = '\033[93m'
    FAIL = '\033[91m'
    normalWhiteText = '\033[0m'
    boldText = '\033[1m'
    UNDERLINE = '\033[4m'

# White text represents what you as the player choose to do
def printWhiteText(message: list = []):
    for messagestring in message:
        print(colour.normalWhiteText + messagestring)

# Blue text represents world-building or narration
def printNarrationText(message: list = []):
    for messagestring in message:
        print(colour.blueText + messagestring)

# Green text represents choices that the narrator has given you
def printChoiceText(message: list = []):
    for messagestring in message:
        print(colour.greenText + messagestring)

# Yellow text represents invalid choices or warnings
def printWarningText(message: list = []):
    for messagestring in message:
        print(colour.yellowText + messagestring)

# Bold text represents events (like picking something up and adding it to inventory)
def printGameEventText(message: list = []):
    for messagestring in message:
        print(colour.boldText + colour.yellowText + messagestring)

# Cyan text represents items, inventory items or item descriptions
def printItemText(message: list = []):
    for messagestring in message:
        print(colour.cyanText + messagestring)

#just displays the "choose" message, and lets us get the players input
def getInput(message):
    return input(colour.normalWhiteText + message)

def resetColorToWhite():
    print(colour.normalWhiteText)