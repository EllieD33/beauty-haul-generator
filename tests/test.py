# File for unit tests.
import unittest
import csv
import os

from user_input import InputValidator
from routine_display import RoutineDisplay, UserHappiness
from db_utils import save_routine


class TestInputValidator(unittest.TestCase):
    def test_validate_yes_no(self):
        self.assertTrue(InputValidator.validate_yes_no("Y"))
        self.assertTrue(InputValidator.validate_yes_no("n"))
        self.assertFalse(InputValidator.validate_yes_no("yes"))
        self.assertFalse(InputValidator.validate_yes_no("No"))
        self.assertFalse(InputValidator.validate_yes_no(""))

class TestIsUserHappy(unittest.TestCase):
    def test_is_user_happy(self):
        self.assertTrue(UserHappiness.ask_if_user_happy(1))
        self.assertTrue(UserHappiness.ask_if_user_happy(2))
        self.assertFalse(UserHappiness.ask_if_user_happy(3))
        self.assertFalse(UserHappiness.ask_if_user_happy("hello"))
        self.assertFalse(UserHappiness.ask_if_user_happy(""))

class TestSavingRoutine(unittest.TestCase):
    def test_save_routine(self):
        test_file = "test_user_routines.csv"
        test_data = [
            {"Category": "Cleanser", "Name": "CeraVe Hydrating Cleanser", "Price": "9.99"},
            {"Category": "MakeUp", "Name": "MAC Ruby Woo Lipstick", "Price": "19.99"}
        ]
        save_routine(test_data, filename=test_file)
        with open(test_file, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["Name"], "CeraVe Hydrating Cleanser")
        self.assertEqual(rows[1]["Price"], "19.99")

        os.remove(test_file)
        print("Test file removed✅")




if __name__ == '__main__':
    unittest.main()
