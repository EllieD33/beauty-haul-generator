# Classes related to gathering and processing user inputs.
from user_preferences import UserPreferences


class UserInputCollector:
    # Ask a single question
    @staticmethod
    def ask_question(question):
        response = input(f"{question}: ")
        return response


# Validation class using static methods
class InputValidator:
    @staticmethod
    def validate_yes_no(response):
        return response.upper() in ["Y", "N"]

    @staticmethod
    def validate_numeric_choices(response, lowest_valid_num, highest_valid_num):
        # Create list of number strings, using given number args
        options = [str(i) for i in range(lowest_valid_num, highest_valid_num + 1)]
        # Check whether the given response is in the valid options list
        return response in options

    @staticmethod
    def validate_string_choices(response, valid_strings_list):
        # Create list of cleaned strings
        options = [i.lower().strip() for i in valid_strings_list]
        # Check whether the given response is in the valid options list
        return response.lower().strip() in options

    @staticmethod
    def validate_complete_numeric_ranking(response, lowest_valid_num, highest_valid_num):
        user_numbers = set(response)
        # Create a set of expected numbers in the specified range
        expected_numbers = {str(i) for i in range(lowest_valid_num, highest_valid_num + 1)}
        # Check that the user's numbers match the expected numbers and there are no duplicates
        return user_numbers == expected_numbers and len(response) == len(user_numbers)


# Class for getting and processing user feedback
class UserFeedbackCollector:
    def __init__(self, input_collector):
        self.input_collector = input_collector

    @staticmethod
    def welcome_user():
        print("\n✨💄 Welcome to the beauty haul generator 💄✨\n")
        print("📌 Here's how this works...\n")
        print("1️⃣ I'll ask some questions about you.")
        print("2️⃣ I'll work my magic to generate you a new haul.")
        print("3️⃣ You can work your own magic armed with your new haul!\n")

    def get_user_consent(self):
        while True:
            response = self.input_collector.ask_question("\n🪄 Shall we get started? Y / N").upper()
            if response == "Y":
                print("\n💫 Let's glow! 💫\n")
                return True
            elif response == "N":
                print("\n❌ No worries! Come back when you're ready to sparkle ✨")
                return False
            else:
                print("⚠️ Please enter 'Y' or 'N'.")

    def is_user_satisfied(self):
        question = "\nWhat do you think? Would you like to save this routine or should we change anything? \n1️⃣ Save routine \n2️⃣ Modify preferences\nPlease enter 1 or 2"
        while True:
            response = self.input_collector.ask_question(question).strip()
            if InputValidator.validate_numeric_choices(response, 1, 2):
                return response == "1"
            else:
                print("⚠️ Invalid input! Please enter 1 or 2")


# Class for collecting and processing user preferences
class UserPreferenceCollector:
    skin_types = ["Dry", "Oily", "Combination", "Normal", "Sensitive"]
    budget_options = ["£", "££", "£££", "££££"]
    product_types = ["Blush", "Bronzer", "Eyebrow", "Eyeliner", "Eyeshadow", "Foundation", "Lip liner", "Lipstick",
                     "Mascara", "Nail Polish"]

    def __init__(self, input_collector):
        self.input_collector = input_collector

    def collect_all_preferences(self):
        preferences = UserPreferences()
        self._collect_skin_type(preferences)
        self._collect_budget(preferences)
        self._collect_product_types(preferences)
        self._collect_priorities(preferences)
        return preferences.preferences_to_dict()

    def _collect_skin_type(self, preferences):
        while True:
            response = self.input_collector.ask_question(
                f"How would you describe your skin type? ({' / '.join(i for i in self.skin_types)})").lower().strip()

            if InputValidator.validate_string_choices(response, self.skin_types):
                preferences.set_skin_type(response)
                print(f"\n✅ Skin type set as: {preferences.get_skin_type()}.")
                break
            else:
                print("⚠️ Please enter a valid skin type.")
                continue

    def _collect_budget(self, preferences):
        while True:
            response = self.input_collector.ask_question(
                f"\nWhat is your current budget? ({', '.join(i for i in self.budget_options)})").strip()
            if InputValidator.validate_string_choices(response, self.budget_options):
                preferences.set_budget(response)
                print(f"\n✅ Budget set as: {preferences.get_budget()}.")
                break
            else:
                print("⚠️ Please enter a valid budget option.")
                continue

    def _collect_product_types(self, preferences):
        products_question = f"\n💄 Which products are you interested in?\nAvailable options: {" / ".join(i for i in self.product_types)}.\nPlease enter chosen products separated by commas. Hit enter when done!\nDesired products"
        while True:
            response = self.input_collector.ask_question(products_question).strip().lower()
            if not response:
                print("\n⚠️ Please enter valid products, separated by commas (e.g. 'lipstick, nail polish")
                continue

            selected_products = [p.strip() for p in response.split(',') if p.strip()]
            invalid = [p for p in selected_products if
                       not InputValidator.validate_string_choices(p, self.product_types)]

            if invalid:
                print(f"\n⚠️ Invalid product(s): {', '.join(invalid)}. Please try again.")
                continue

            preferences.set_product_type(selected_products)
            print(f"\n✅ Desired product types successfully set as: {preferences.get_product_preference()}.")
            break

    def _collect_priorities(self, preferences):
        rank_importance_question = f"\n⚖️ Rank these in order of importance to you: 1. Budget / 2. Vegan-friendly / 3. Eco-friendly / 4. Natural ingredients.\nWrite the numbers in order of importance, starting with the most important (e.g., 3, 2, 1, 4)"
        while True:
            response = self.input_collector.ask_question(rank_importance_question)
            if not response:
                print("\n⚠️ Please enter valid numbers, separated by commas (e.g. '1, 3, 4, 2")
                continue

            cleaned_response = [num.strip() for num in response.split(',') if num.strip()]
            valid = True
            if not InputValidator.validate_complete_numeric_ranking(cleaned_response, 1, 4):
                valid = False
            for num in cleaned_response:
                if not InputValidator.validate_numeric_choices(num, 1, 4):
                    valid = False
                    break

            if valid:
                preferences.set_priorities(cleaned_response)
                print(f"\n✅ Ranking successful.")
                break
            else:
                print("⚠️ Please enter valid numbers, separated by commas (e.g. '1, 3, 4, 2')")
