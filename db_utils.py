# File containing utility functions for accessing database.
import csv
import os.path


def save_routine(routine, filename="data/user_routines.csv"):
    headers = ["Brand", "Product", "Price", "Description"]
    #check if file exists
    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="") as csv_file:
        writer=csv.DictWriter(csv_file, fieldnames=headers)

        #if the file is empty, write the headers
        if not file_exists or os.path.getsize(filename) == 0:
            writer.writeheader()

        writer.writerows(routine)
    print("Your routine has been saved successfully!💾")
