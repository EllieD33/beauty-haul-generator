# File containing utility functions for accessing database.
import csv


def save_routine(routine, filename="data/user_routines.csv"):
    headers = ["Category", "Name", "Price"]
    with open(filename, "a") as csv_file:
        writer=csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(routine)
    print("Your routine has been saved successfully!💾")
