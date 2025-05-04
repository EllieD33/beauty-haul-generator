# Classes related to displaying the routine and saving the data to DB
import os
import csv
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
    def __init__(self, routine, user_filename):
        self.routine = routine
        self.filename = user_filename
        self.csv_directory = "user_routines"

    def _dir_exists(self):
        if not os.path.exists(self.csv_directory):
            os.makedirs(self.csv_directory)

    def save_to_csv(self):
        headers = ["Brand", "Product", "Price", "Description", "Score"]
        routine_dict = [
            {header: product_dict.get(header, "") for header in headers}
            for product in self.routine
            for product_dict in [product.routine_to_dict()]
        ]

        try:
            self._dir_exists()

            file_name = f"{self.csv_directory}/{self.filename}.csv"
            file_exists = os.path.exists(file_name)

            with open(file_name, "a", newline="") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers)

                # If the file is new or empty, write headers
                if not file_exists or os.path.getsize(file_name) == 0:
                    writer.writeheader()

                writer.writerows(routine_dict)

        except Exception as e:
            print(f"Unexpected error occurred: {e}")



    # method to call the save_routine function from db_utils
    def save_routine(self):
        try:
            insert_new_user_routine(self.routine)
            csv_saved = self.save_to_csv()
            if csv_saved:
                print("\n✅ Your beauty routine has been successfully saved! You're glowing! ✨\n")
            else:
                print("Saved to DB")
        except Exception as e:
            print("\n⚠️ Oops, something went wrong while saving your routine. Please try again!\n")
            print(f"(Error: {e})")
            # This function can be swapped for proper logging if the project was to get bigger.
