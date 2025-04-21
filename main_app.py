# This is the client-side of the application.
from routine_display import RoutineDisplay, UserHappiness, SaveRoutine
from user_input import UserInputCollector, InputValidator
from routine_api import get_skin_type_products

#
def get_user_consent(input_collector):
    while True:
        response = input_collector.ask_question("\n🪄 Shall we get started? Y / N")
        if InputValidator.validate_yes_no(response):
            if response.upper() == "Y":
                print("\n💫 Let's glow! 💫\n")
                break
            else:
                print("\n❌ No worries! Come back when you're ready to sparkle ✨")
                return
        else:
            print("⚠️ Please enter 'Y' or 'N'.")

def is_user_happy(routine, question="What do you think? Would you like to save this routine or should we change anything?"):
    while True:
        print(question)
        print(f"1️⃣Save routine")
        print(f"2️⃣Modify preferences")
        try:
            user_choice = int(input("Please enter 1 or 2: "))
        except ValueError:
            print("⚠️Invalid input! Please enter a number (1 or 2).")
            continue
        output = UserHappiness.ask_if_user_happy(user_choice)
        if output == "save":
            return output
        elif output == "modify":
            return output


def main():
    print("\n✨💄 Welcome to the beauty haul generator 💄✨\n")
    print("📌 Here's how this works...\n")
    print("1️⃣ I'll ask some questions about you.")
    print("2️⃣ I'll work my magic to generate you a new haul.")
    print("3️⃣ You can work your own magic armed with your new haul!\n")

    input_collector = UserInputCollector()

    get_user_consent(input_collector)

    # get user preferences -- practice to check works with RoutineDisplay class
    # print("lets get the users preferences")
    # skin_type = "normal"
    # limit = 5
    # responses = {"skin_type": skin_type, "limit": limit}

    # get API generated routine
    routine = get_skin_type_products(skin_type, limit)

    routine_display = RoutineDisplay(routine, responses)

    # display output functions
    routine_display.check_if_routine_empty()
    if routine:
        routine_display.display_title()
        routine_display.display_routine()


    is_user_happy(routine)



if __name__ == "__main__":
    main()
