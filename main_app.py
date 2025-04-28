# This is the client-side of the application.
from advanced_filtering import AdvancedFilter
from routine_display import RoutineDisplay, UserHappiness, SaveRoutine
from ui.loading_spinner import Spinner
from user_input import UserInputCollector, InputValidator
from routine_api import get_skin_type_products
from user_preferences import UserPreferences


def print_welcome_screen():
    print("\n✨💄 Welcome to the beauty haul generator 💄✨\n")
    print("📌 Here's how this works...\n")
    print("1️⃣ I'll ask some questions about you.")
    print("2️⃣ I'll work my magic to generate you a new haul.")
    print("3️⃣ You can work your own magic armed with your new haul!\n")


def get_user_consent(input_collector):
    while True:
        response = input_collector.ask_question("\n🪄 Shall we get started? Y / N").upper()
        if response == "Y":
            print("\n💫 Let's glow! 💫\n")
            return True
        elif response == "N":
            print("\n❌ No worries! Come back when you're ready to sparkle ✨")
            return False
        else:
            print("⚠️ Please enter 'Y' or 'N'.")


def is_user_satisfied(input_collector):
    question = "\nWhat do you think? Would you like to save this routine or should we change anything? \n1️⃣ Save routine \n2️⃣ Modify preferences\nPlease enter 1 or 2"

    response = input_collector.ask_question(question).strip()
    if InputValidator.validate_numeric_choices(response, 1, 2):
        return UserHappiness.is_satisfied(response)
    else:
        print("⚠️ Invalid input! Please enter 1 or 2")

def collect_user_preferences(input_collector):
    preferences = UserPreferences()
    # input_collector = UserInputCollector()

    #Outline valid product types
    skin_types = ["Dry", "Oily", "Combination", "Normal", "Sensitive"]
    budget_options = ["£", "££", "£££", "££££"]
    product_types = ["Blush", "Bronzer", "Eyebrow", "Eyeliner", "Eyeshadow", "Foundation", "Lip liner", "Lipstick", "Mascara", "Nail Polish"]

    # Get user skin type
    while True:
        response = input_collector.ask_question(f"How would you describe your skin type? ({' / '.join(i for i in skin_types)})").lower().strip()

        if InputValidator.validate_string_choices(response, skin_types):
            preferences.set_skin_type(response)
            print(f"\n✅ Skin type set as: {preferences.get_skin_type()}.")
            break
        else:
            print("⚠️ Please enter a valid skin type.")
            continue

    # Get user budget
    while True:
        response = input_collector.ask_question(f"\nWhat is your current budget? ({', '.join(i for i in budget_options)})").strip()
        if InputValidator.validate_string_choices(response, budget_options):
            preferences.set_budget(response)
            print(f"\n✅ Budget set as: {preferences.get_budget()}.")
            break
        else:
            print("⚠️ Please enter a valid budget option.")
            continue

    # Collect product types
    products_question = f"\n💄 Which products are you interested in?\nAvailable options: {" / ".join(i for i in product_types)}.\nPlease enter chosen products separated by commas. Hit enter when done!\nDesired products"

    while True:
        response = input_collector.ask_question(products_question).strip().lower()
        if not response:
            print("\n⚠️ Please enter valid products, separated by commas (e.g. 'lipstick, nail polish")
            continue

        selected_products = [p.strip() for p in response.split(',') if p.strip()]
        invalid = [p for p in selected_products if not InputValidator.validate_string_choices(p, product_types)]

        if invalid:
            print(f"\n⚠️ Invalid product(s): {', '.join(invalid)}. Please try again.")
            continue

        preferences.set_product_type(selected_products)
        print(f"\n✅ Desired product types successfully set as: {preferences.get_product_preference()}.")
        break

    rank_importance_question = f"\n⚖️ Rank these in order of importance to you: 1. Budget / 2. Vegan-friendly / 3. Eco-friendly / 4. Natural ingredients.\nWrite the numbers in order of importance, starting with the most important (e.g., 3, 2, 1, 4)"
    while True:
        response = input_collector.ask_question(rank_importance_question)
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

    # # Collect brand preferences.
    # print("\n🏷️ Do you have any favorite brands?")
    # print("\nAvailable brands: Almay / Alva / Anna Sui / Annabelle / Benefit / Boosh / Burt's Bees / Butter London")
    # print("C'est Moi / Cargo Cosmetics / China Glaze / Clinique / Coastal Classic Creation / Colourpop")
    # print("Covergirl / Danish / Deciem / Dior / Dr. Hauschka / E.L.F / Essie / Fenty / Glossier")
    # print("Green People / Iman / L'Oreal / Lotus Cosmetics / Maia's Mineral Galaxy / Marcelle")
    # print("Marienatie / Maybelline / Milani / Mineral Fusion / Misa / Mistura / Moov / Nudus / Nyx")
    # print("Orly / Pacifica / Penny Lane Organics / Physicians Formula / Piggy Paint / Pure Anada")
    # print("Rejuva Minerals / Revlon / Sally B's Skin Yummies / Salon Perfect / Sante / Sinful Colours")
    # print("Smashbox / Stila / Suncoat / W3llpeople / Wet n Wild / Zorah / Zorah Biocosmetiques")
    # print("\nPlease enter chosen brands separated by commas, or press enter to skip.")
    #
    # while True:
    #     brand_input = input("Desired brands: ").strip()
    #     if not brand_input:
    #         print("🥳Looks like you're happy to try all of our brands!")
    #         break
    #
    #     brands = brand_input.split(',')
    #     all_brands_valid = True
    #
    #     for brand in brands:
    #         if not preferences.add_brand_preference(brand.strip()):
    #             print(f"\n⚠️ '{brand.strip()}' is not a valid brand. Please try again.")
    #             all_brands_valid = False
    #             preferences.__brand_preference = []
    #             break
    #
    #     if all_brands_valid:
    #         print("\n✅ Brand(s) successfully added!")
    #         break
    return preferences.preferences_to_dict()


def generate_routine(user_responses):
    # Get products for users skin-type
    product_list = get_skin_type_products(user_responses["skin_type"])
    routine_filter = AdvancedFilter

    # Remove product types the user has not specified as part of their routine
    relevant_products = routine_filter.filter_product_types(user_responses["product_types"], product_list)

    refined_product_list = []

    # Apply advanced filtering for each product type user wants in their routine
    for product_type in user_responses["product_types"]:
        filtered_products = routine_filter.filter_by_relevance(
            user_responses["priorities"], product_type, user_responses["budget"], relevant_products
        )

        # Add the filtered products to the refined list
        refined_product_list.extend(filtered_products)

    # Ensure no duplicates
    refined_product_list = list(set(refined_product_list))

    return refined_product_list



def main():
    print_welcome_screen()
    input_collector = UserInputCollector()
    if not get_user_consent(input_collector):
        return
    user_responses = collect_user_preferences(input_collector)

    app_spinner = Spinner(message="Generating your beauty haul")
    app_spinner.start()
    try:
        routine = [product for product in generate_routine(user_responses)]
    finally:
        app_spinner.stop()

    routine_display = RoutineDisplay(routine, user_responses)

    # Display output functions
    routine_display.check_if_routine_empty()
    if routine:
        routine_display.display_title()
        routine_display.display_routine()

    # Check if user is satisfied with recommended routine
    if is_user_satisfied(input_collector):
        routine_saver = SaveRoutine(routine)
        routine_saver.save_routine()
        print("Thank you for using the beauty generator, you're glowing with your new routine! ✨")
    else:
        print("Don't worry, lets start again!✨")
        main()


if __name__ == "__main__":
    main()
