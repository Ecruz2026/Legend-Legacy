# Emmanuel Cruz

# Nov 24, 2024

# Print the options

# Ask user to input

# Send user to different branch based on choice


def chapter_3():
    print("Chapter 3: The Next Step")
    print("You find yourself standing before a peculiar spot in a dimly lit tunnel.")
    print("Something about the ground catches your eye—it looks disturbed.")

    options = ["Dig up the spot","Return home"]
        

    while True:
        print("\nPlease choose an option:")
        for index, option in enumerate(options):
            print(f"{index + 1}. {option.capitalize()}")

        choice = input("Enter the option number (1-2): ")

        if choice == "1":
            dig_choice = input("Do you want to dig up the spot? (yes/no): ").strip().lower()
            if dig_choice == "yes":
                print("\nYou dig up the spot and find a key to a door!")
                print("You have found a key! You can now proceed to Chapter 4.")
                # Proceed to Chapter 4 logic here
                break  # Exit the loop as user advances to Chapter 4
            elif dig_choice == "no":
                print("\nYou chose not to dig. The key disappears.")
                print("Game Over. You must restart the game.")
                break  # Exit the loop and game over

        elif choice == "2":
            return_home = input("Do you want to return home? (yes/no): ").strip().lower()
            if return_home == "yes":
                print("\nYou return home, but the key disappears.")
                print("Game Over. You must restart the game.")
                break  # Exit the loop and game over
            elif return_home == "no":
                print("\nYou decide to go back to the spot in the tunnel and reconsider your options.")
                continue  # Loop back to the options

        else:
            print("\nInvalid choice. Please select option 1 or 2.")

# Start the game at Chapter 3
chapter_3()