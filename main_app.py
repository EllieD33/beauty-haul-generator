# This is the client-side of the application.
from user_input import UserInputCollector, InputValidator


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


def main():
    print("\n✨💄 Welcome to the beauty haul generator 💄✨\n")
    print("📌 Here's how this works...\n")
    print("1️⃣ I'll ask some questions about you.")
    print("2️⃣ I'll work my magic to generate you a new haul.")
    print("3️⃣ You can work your own magic armed with your new haul!\n")

    input_collector = UserInputCollector()

    get_user_consent(input_collector)


if __name__ == "__main__":
    main()
