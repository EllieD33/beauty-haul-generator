# Classes related to displaying the routine and saving the data to DB

from data.db_utils import insert_new_user_routine


# equals sign decorator to surround the display title in the terminal
def equal_sign_decorator(func):
    def inner(*args, **kwargs):
        print("\n")
        print("=" * 40)
        func(*args, **kwargs)
        print("=" * 40)
        print("\n")

    return inner

# class for displaying the routine to the terminal
class RoutineDisplay:
    def __init__(self, routine, responses):
        self.routine = routine
        self.responses = responses

    # check if the routine is empty
    def check_if_routine_empty(self):
        if not self.routine:
            print(
                f"\n\nOops, we couldn't find any products that matched your preferences! Maybe we can alter something and try again? 🔄")
            return

    # if a routine is present, methods to display the title and display the routine from the API
    @staticmethod
    @equal_sign_decorator
    def display_title():
        print("✨Here is your personalised beauty routine!✨")

    def display_routine(self):
        print(f"Based on your preferences of {self.responses}, this is what we have chosen: ")
        for product in self.routine:
            product.display_info()

# class to save the routine to the DB
class SaveRoutine:
    def __init__(self, routine):
        self.routine = routine

    # method to call the save_routine function from db_utils
    def save_routine(self):
        try:
            insert_new_user_routine(self.routine)
            print("\n✅ Your beauty routine has been successfully saved! You're glowing! ✨\n")
        except Exception as e:
            print("\n⚠️ Oops, something went wrong while saving your routine. Please try again!\n")
            print(f"(Error: {e})")
            # This function can be swapped for proper logging if the project was to get bigger.


