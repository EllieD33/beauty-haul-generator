# File containing utility functions for accessing database.
import os
import csv

def save_routine(routine, filename="data/user_routines.csv"):
    headers = ["Brand", "Product", "Price", "Description", "Score"]

    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Create a list of dictionaries for the routine
    routine_dict = [
        {header: product_dict.get(header, "") for header in headers}
        for product in routine
        for product_dict in [product.routine_to_dict()]
    ]

    try:
        file_exists = os.path.exists(filename)

        with open(filename, "a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)

            # If the file is new or empty, write headers
            if not file_exists or os.path.getsize(filename) == 0:
                writer.writeheader()

            writer.writerows(routine_dict)

        print("\nYour routine has been saved successfully! 💾")

    except Exception as e:
        print(f"⚠️ Error: An unexpected error occurred: {e}")


