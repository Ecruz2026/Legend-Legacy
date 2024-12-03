# Emmanuel Cruz

# Nov 24, 2024

# Print the options

# Ask user to input

# Send user to different branch based on choice

def chapter_4():
    print("Chapter 4: The Mysterious Book")
    print("You find yourself in a dimly lit room with a mysterious book on a pedestal.")
    print("You can feel a strange energy emanating from it.")

    options = [ "Look at the book","Leave the room to go outside"]


    while True:
        print("\nPlease choose an option:")
        for index, option in enumerate(options):
            print(f"{index + 1}. {option.capitalize()}")

        choice = input("Enter the option number (1-2): ")

        if choice == "1":
            look_at_book = input("Do you want to look at the book? (yes/no): ").strip().lower()
            if look_at_book == "yes":
                print("\nYou open the book and discover the truth about your journey!")
                print("With knowledge in hand, you are now ready to proceed to Chapter 5.")
                # Proceed to Chapter 5 logic here
                break  # Exit the loop as user advances to Chapter 5
            elif look_at_book == "no":
                print("\nYou chose not to grab the book. Suddenly, it bursts into flames!")
                print("Game Over. You must restart the game.")
                break  # Exit the loop and game over

        elif choice == "2":
            leave_room = input("Do you want to leave the room? (yes/no): ").strip().lower()
            if leave_room == "yes":
                print("\nYou open the door and step outside, but it slams shut behind you.")
                print("The door is locked and will never open again.")
                print("Game Over. You must restart the game.")
                break  # Exit the loop and game over
            elif leave_room == "no":
                print("\nYou decide to stay and look for clues.")
                continue  # Loop back to the options

        else:
            print("\nInvalid choice. Please select option 1 or 2.")

# Start the game at Chapter 4
chapter_4()