# Emmanuel Cruz

# Nov 24, 2024

# Print the options

# Ask user to input

# Send user to different branch based on choice

def chapter_1():
    print("\nYou go back into Chapter 1 to rethink your decisions.")
    print("You have returned to Chapter 1.")

def chapter_5():
    print("Chapter 5: The Final Revelation")
    print("You stand before the villagers, knowing the truth about your identity as the son of the king.")

    options = ["Speak to the villagers about being the son of the king", "Keep this truth a secret"]
        
    while True:
        print("\nPlease choose an option:")
        for index, option in enumerate(options):
            print(f"{index + 1}. {option.capitalize()}")

        choice = input("Enter the option number (1-2): ")

        if choice == "1":
            speak_to_villagers = input("Do you want to speak to the villagers? (yes/no): ").strip().lower()
            if speak_to_villagers == "yes":
                print("\nThe villagers look at you with disbelief. They think you are crazy.")
                chapter_1()  # Call Chapter 1 here
                return  # Exit the chapter, returning to Chapter 1
            elif speak_to_villagers == "no":
                print("\nYou decide to keep your mouth shut for now.")
                print("The game ends here. You have chosen wisely to keep your secret.")
                break  # End the game here

        elif choice == "2":
            keep_secret = input("Do you want to keep this truth a secret? (yes/no): ").strip().lower()
            if keep_secret == "yes":
                print("\nYou hold on to the secret and live happily, knowing the truth.")
                print("The game ends here. You have chosen wisely to keep your secret.")
                break  # End the game here
            elif keep_secret == "no":
                print("\nYou tell some villagers about your true identity.")
                print("They don't believe you and think you are crazy.")
                chapter_1()  # Call Chapter 1 here
                return  # Exit the chapter, returning to Chapter 1
            
        else:
            print("\nInvalid choice. Please select option 1 or 2.")

# Start the game at Chapter 5 initially
chapter_5()