def intro_scene():
    print("You find yourself in a dimly lit tunnel.")
    print("You see three paths ahead: left, right, and straight.")
    choice = input("Which way do you want to go? (left/right/straight): ")

    if choice.lower() == "left":
        print("You encounter a locked door. You need a key.")
        # Add more logic for this path
    elif choice.lower() == "right":
        print("You hear distant footsteps. Someone is coming!")
        # Add more logic for this path
    elif choice.lower() == "straight":
        print("You see a faint light at the end of the tunnel.")
        # Add more logic for this path
    else:
        print("Invalid choice. Try again.")
        intro_scene()  # Repeat the intro scene

# Add more scenes and choices as needed

if __name__ == "__main__":
    # Initialize the game
    print("Welcome to the Adventure Game!")
    print("...")
    player_name = input("Enter your name: ")
    print(f"Good luck, {player_name}!")
    intro_scene()
