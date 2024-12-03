# Emmanuel Cruz

# Nov 24, 2024

# Print the options

# Ask user to input

# Send user to different branch based on choice

def chapter1():
    print("\nChapter 1: Welcome back to the village!")
    
    options = ["Start interacting", "Go shopping in the village market", "Go back home", "Go explore"]
       
    while True:  # Loop until the user chooses to explore the forest
        print("\nPlease choose an option:")
        for index, option in enumerate(options):
            print(f"{index + 1}. {option.capitalize()}")
        
        choice = input("Enter the option number (1-4): ")

        if choice == "1":
            print("\nYou chose to start interacting with the villagers.")
            while True:
                decision = input("Do you want to continue interacting? (yes/no): ").lower()
                if decision == 'yes':
                    print("Gain info on the village.")
                    break  # Go back to options
                elif decision == 'no':
                    print("You decided to stop interacting.")
                    break  # Go back to options
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")
        
        elif choice == "2":
            print("\nYou chose to go shopping in the village market.")
            while True:
                decision = input("Will you buy heals? (yes/no): ").lower()
                if decision == 'yes':
                    print("Get bread and water as healing.")
                    break  # Go back to options
                elif decision == 'no':
                    print("Get nothing and continue on exploring.")
                    break  # Go back to options
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")
        
        elif choice == "3":
            print("\nYou chose to go back home.")
            while True:
                decision = input("Do you want to stay home? (yes/no): ").lower()
                if decision == 'yes':
                    print("Get rest and get ready to explore tomorrow.")
                    break  # Go back to options
                elif decision == 'no':
                    print("You go and explore the village.")
                    break  # Go back to options
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")

        elif choice == "4":
            print("\nYou chose to go explore the Forgotten Forest.")
            decision = input("Go to the forest to find clues? (yes/no): ").lower()
            if decision == 'yes':
                print("You went to the forest.")
                print("\nChapter 2: The Forgotten Forest")
                print("You find yourself deep in the Forgotten Forest.")
                print("The adventure continues...")
                break  # Exit the loop to indicate transition to Chapter 2
            elif decision == 'no':
                print("You go back to your home.")
                continue  # Loop back to options
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
        
        else:
            print("Invalid choice. Please select a valid option (1-4).")

# Start the game by calling chapter1()
chapter1()