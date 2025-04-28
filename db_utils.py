# File containing utility functions for accessing database.
import os
import csv

def save_routine(routine, filename="data/user_routines.csv"):
    headers = ["Brand", "Product", "Price", "Description"]
    routine_dict = []
    # Create a dictionary from each product in the same routine
    for product, score in routine:
        try:
            product_dict = product.routine_to_dict() # convert the products to a dictionary
            product_values = list(product_dict.values())
            each_row = dict(zip(headers,product_values)) # combine the headers with the values in each row
            routine_dict.append(each_row)
        except AttributeError as e:
            print(f"⚠️ Error processing product: {e}")
            continue # skip problematic product if an error occurs

    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        file_exists = os.path.exists(filename)

        with open(filename, "a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)

            # If the file is empty, write headers
            if not file_exists or os.path.getsize(filename) == 0:
                writer.writeheader()

            writer.writerows(routine_dict)

        print("\nYour routine has been saved successfully! 💾")

    except PermissionError:
        print(f"⚠️ Error: Insufficient permissions to save to {filename}.")
    except FileNotFoundError:
        print(f"⚠️ Error: The file path {filename} does not exist.")
    except Exception as e:
        print(f"⚠️ Error: An unexpected error occurred: {e}")


