# Classes related to displaying the routine and saving the data

from db_utils import save_routine
from products import Product
from routine_api import get_skin_type_products


# equals sign decorator to surround the display title
def equal_sign_decorator(func):
    def inner(*args, **kwargs):
        print("=" * 40)
        func(*args, **kwargs)
        print("=" * 40)

    return inner


class RoutineDisplay:
    def __init__(self, routine, responses):
        self.routine = routine
        self.responses = responses

    # check if the routine is empty
    def check_if_routine_empty(self):
        if not self.routine:
            print(
                f"Oops, we couldn't find any products that matched your preferences! Maybe we can alter something and try again? 🔄")
            return

    @staticmethod
    @equal_sign_decorator
    def display_title():
        print("✨Here is your personalised beauty routine!✨")

    def display_routine(self):
        # loop through the products in the routine dictionary / list and print each

        print(f"Based on your preferences of {self.responses}, this is what we have chosen: ")
        for product, score in self.routine:
            product.display_info()
            print(f"Compatibility score: {score}\n")
            # print(f"Category: {product['category']}")
            # print(f"Name: {product['name']}")
            # print(f"Price: {product['price']}")
            # print(f"Match score for your skin type: {score}")


class UserHappiness:
    @staticmethod
    def is_satisfied(response):
        return response.strip() == "1"


class SaveRoutine:
    def __init__(self, routine, filename="data/user_routines.csv"):
        self.routine = routine
        self.filename = filename

    def save_routine(self):
        try:
            save_routine(self.routine, filename=self.filename)
            print("\n✅ Your beauty routine has been successfully saved! You're glowing! ✨\n")
        except Exception as e:
            print("\n⚠️ Oops, something went wrong while saving your routine. Please try again!\n")
            # Optionally, if you want to log the error details for developers:
            # print(f"Debug info: {e}"
            # This function can be swapped for proper logging if the project was to get bigger.


