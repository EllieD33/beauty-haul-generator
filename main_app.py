# This is the client-side of the application.
from routine_display import RoutineDisplay, UserHappiness, SaveRoutine
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

def collect_user_preferences():
    preferences = UserPreferences()
    input_collector = UserInputCollector()

    #Outline valid product types
    product_types = ["Blush", "Bronzer", "Eyebrow", "Eyeliner", "Eyeshadow", "Foundation", "Lip liner", "Lipstick", "Mascara", "Nail Polish"]


    # Get user skin type
    while True:
        skin_type = input_collector.ask_question("How would you describe your skin type? (Dry / Oily / Combination / Normal / Sensitive)").lower()
        if preferences.set_skin_type(skin_type):
            break
        print("⚠️Please enter a skin type from the available options.")

    # Get user budget
    while True:
        budget = input_collector.ask_question("\nWhat is your current budget? (£ / ££ / £££ / ££££)")
        if preferences.set_budget(budget):
            break
        print("⚠️Please enter a valid budget option.")

    # Collect product types
    print("\n💄 Which products are you interested in?")
    print("\nAvailable options: Blush / Bronzer / Eyebrow / Eyeliner / Eyeshadow / Foundation / Lip liner / Lipstick / Mascara / Nail Polish")
    print("\nPlease enter chosen products separated by commas. Hit enter when done!")

    while True:
        product_input = input("Desired products: ").strip()
        if not product_input:
            print("\n⚠️ Please enter valid products, separated by commas (e.g. 'Lipstick, Nail polish")
            continue

        selected_products = []
        for p in product_input.split(','):
            product = p.strip()
            available_product = next((pt for pt in product_types if pt.lower() == product.lower()),None)
            if available_product:
                selected_products.append(available_product)
            else:
                print(f"\n⚠️ '{product}' is not a valid product type.")
                break
        else:
            if selected_products:
                preferences.set_product_type(selected_products)
                break
            else:
                print("\n⚠️ Please enter️ valid products, which must be separated by a comma.")

    # Collect brand preferences.
    print("\n🏷️ Do you have any favorite brands?")
    print("\nAvailable brands: Almay / Alva / Anna Sui / Annabelle / Benefit / Boosh / Burt's Bees / Butter London")
    print("C'est Moi / Cargo Cosmetics / China Glaze / Clinique / Coastal Classic Creation / Colourpop")
    print("Covergirl / Danish / Deciem / Dior / Dr. Hauschka / E.L.F / Essie / Fenty / Glossier")
    print("Green People / Iman / L'Oreal / Lotus Cosmetics / Maia's Mineral Galaxy / Marcelle")
    print("Marienatie / Maybelline / Milani / Mineral Fusion / Misa / Mistura / Moov / Nudus / Nyx")
    print("Orly / Pacifica / Penny Lane Organics / Physicians Formula / Piggy Paint / Pure Anada")
    print("Rejuva Minerals / Revlon / Sally B's Skin Yummies / Salon Perfect / Sante / Sinful Colours")
    print("Smashbox / Stila / Suncoat / W3llpeople / Wet n Wild / Zorah / Zorah Biocosmetiques")
    print("\nPlease enter chosen brands separated by commas, or press enter to skip.")

    while True:
        brand_input = input("Desired brands: ").strip()
        if not brand_input:
            print("🥳Looks like you're happy to try all of our brands!")
            break

        brands = brand_input.split(',')
        all_brands_valid = True

        for brand in brands:
            if not preferences.add_brand_preference(brand.strip()):
                print(f"\n⚠️ '{brand.strip()}' is not a valid brand. Please try again.")
                all_brands_valid = False
                preferences.__brand_preference = []
                break

        if all_brands_valid:
            print("\n✅ Brand(s) successfully added!")
            break

    return preferences

def main():
    print_welcome_screen()
    input_collector = UserInputCollector()
    if get_user_consent(input_collector):
        user_preferences = collect_user_preferences()
    else:
        return

    skin_type = "normal"
    limit = 5
    responses = {"skin_type": skin_type, "limit": limit}

    # get API generated routine
    routine = get_skin_type_products(skin_type, limit)

    routine_display = RoutineDisplay(routine, responses)

    # display output functions
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
        # Then call the refinement flow (or start again?)


if __name__ == "__main__":
    main()
