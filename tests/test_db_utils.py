import unittest
import csv
import os

from db_utils import save_routine

class MockProduct:
    def __init__(self, data):
        self.data = data

    def routine_to_dict(self):
        return self.data

class TestSavingRoutine(unittest.TestCase):
    def test_save_routine(self):
        test_file = "test_user_routines.csv"
        test_data_dicts = [
            {"Brand": "Fenty", "Product": "Foundation", "Price": "30", "Description": "Test description", "Score": 4},
            {"Brand": "MAC", "Product": "Lipstick", "Price": "19.99", "Description": "MAC Ruby Woo Lipstick",
             "Score": 8}
        ]
        test_data = [MockProduct(mock) for mock in test_data_dicts]
        save_routine(test_data, filename=test_file)
        with open(test_file, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
            for row in rows:
                print(row)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["Product"], "Foundation")
        self.assertEqual(rows[1]["Price"], "19.99")

    def tearDown(self):
        test_file = "test_user_routines.csv"
        if os.path.exists(test_file):
            os.remove(test_file)
            print("Test file removed ✅")
        else:
            print("No test file found, no removal needed")


if __name__ == '__main__':
    unittest.main()
