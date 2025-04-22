# File containing utility functions for accessing database.
import csv
import os.path


def save_routine(routine, filename="data/user_routines.csv"):
    headers = ["Brand", "Product", "Price", "Description"]
    # create a list of dictionaries for the routine
    routine_dict = []
    for product, score in routine:
        product_dict = product.routine_to_dict() # convert the products to a dictionary
        product_values = list(product_dict.values())
        each_row = dict(zip(headers,product_values)) # combine the headers with the values in each row
        routine_dict.append(each_row)
    #check if file exists
    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="") as csv_file:
        writer=csv.DictWriter(csv_file, fieldnames=headers)

        #if the file is empty, write the headers
        if not file_exists or os.path.getsize(filename) == 0:
            writer.writeheader()

        writer.writerows(routine)
    print("Your routine has been saved successfully!💾")
