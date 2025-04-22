# This is the client-side of the application.
from user_input import UserInputCollector, InputValidator


def print_welcome_screen():
    print("\n✨💄 Welcome to the beauty haul generator 💄✨\n")
    print("📌 Here's how this works...\n")
    print("1️⃣ I'll ask some questions about you.")
    print("2️⃣ I'll work my magic to generate you a new haul.")
    print("3️⃣ You can work your own magic armed with your new haul!\n")


def get_user_consent(input_collector):
    while True:
        response = input_collector.ask_question("\n🪄 Shall we get started? Y / N").strip().upper()
        if InputValidator.validate_yes_no(response):
            if response == "Y":
                print("\n💫 Let's glow! 💫\n")
                break
            else:
                print("\n❌ No worries! Come back when you're ready to sparkle ✨")
                return
        else:
            print("⚠️ Invalid input! Please enter 'Y' or 'N'.")


def is_user_satisfied(input_collector):
    question = "\nWhat do you think? Would you like to save this routine or should we change anything? \n1️⃣ Save routine \n2️⃣Modify preferences\nPlease enter 1 or 2: "

    response = input_collector.ask_question(question).strip()
    if InputValidator.validate_numeric_choices(response, 1, 2):
        if response == "1":
            return True
        else:
            return False
    else:
        print("⚠️ Invalid input! Please enter 1 or 2")



def main():
    print_welcome_screen()
    input_collector = UserInputCollector()
    get_user_consent(input_collector)
    if is_user_satisfied(input_collector):
        print("Thank you for using the beauty generator, you're glowing with your new routine! ✨")
        pass # Call the save routine method
    else:
        print("Don't worry, lets start again!✨")
        pass # Call the refinement flow (or start again?)




if __name__ == "__main__":
    main()
