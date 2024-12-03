# Emmanuel Cruz

# Nov 24, 2024

# Print the options

# Ask user to input

# Send user to different branch based on choice


# Define a function to represent Chapter 1 for navigation
def chapter1():
    print("\nWelcome to Chapter 1! The adventure begins...")
    # Implement Chapter 1 story and options here, for simplicity we'll just end it for now.
    print("You have returned to Chapter 1.")


def chapter2():
    print("\nWelcome to Chapter 2: The Forgotten Forest!")

    options = ["Check out the boulder", "Ignore the boulder", "Go back to the village"]

    while True:
        print("\nPlease choose an option:")
        for index, option in enumerate(options):
            print(f"{index + 1}. {option.capitalize()}")

        choice = input("Enter the option number (1-3): ")

        if choice == "1":
            if check_boulder():  # If the player finds the note or opts not to check it, go to Chapter 1 or Chapter 3
                break  # Exit Chapter 2 as options are no longer displayed
        elif choice == "2":
            if not ignore_boulder():  # If player dies, game over
                break  # Exit and end the game
        elif choice == "3":
            if not go_back_to_village():  # If player chooses to go back or dies, options no longer available
                break  # Exit and end the game
        else:
            print("Invalid choice. Please select a valid option (1-3).")

def check_boulder():
    print("\nYou approach a large, mysterious boulder.")
    decision = input("Do you want to check out the boulder? (yes/no): ").lower()
    if decision == 'yes':
        print("You find a note tucked under the boulder!")
        print("The note says there is a tunnel in the village.")
        print("Chapter 3 begins...")
        return True  # Indicate that the transition to Chapter 3 has occurred
    elif decision == 'no':
        print("You choose not to check the boulder and miss the note.")
        print("You turn around and head back home.")
        chapter1()  # Redirect to Chapter 1
        return True  # Indicate return to Chapter 1
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        return check_boulder()  # Re-prompt if input is invalid

def ignore_boulder():
    print("\nYou choose to ignore the boulder.")
    while True:
        decision = input("Do you want to continue on your path? (yes/no): ").lower()
        if decision == 'yes':
            print("You wander off into the woods...")
            print("Unfortunately, you get lost and die due to hunger. GAME OVER.")
            return False  # Game Over
        elif decision == 'no':
            print("You decide to go back to find clues.")
            break  # Go back to options
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
    return True  # Go back to options for a new choice 

def go_back_to_village():
    print("\nYou consider going back to the village.")
    while True:
        decision = input("Do you want to go back to the village? (yes/no): ").lower()
        if decision == 'yes':
            print("You return to the village safely.")
            chapter1()  # Redirect to Chapter 1
            return False  # Indicate options in Chapter 2 should no longer be available
        elif decision == 'no':
            print("You decide to stay out here.")
            print("Unfortunately, you get lost and die due to hunger. GAME OVER.")
            return False  # Game Over
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


# Main program execution starts here
chapter2()