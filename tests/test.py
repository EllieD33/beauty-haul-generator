# File for unit tests.
import unittest

from user_input import InputValidator


class TestInputValidator(unittest.TestCase):
    def test_validate_yes_no(self):
        self.assertTrue(InputValidator.validate_yes_no("Y"))
        self.assertFalse(InputValidator.validate_yes_no("yes"))
        self.assertFalse(InputValidator.validate_yes_no("No"))
        self.assertFalse(InputValidator.validate_yes_no(""))

    def test_validate_numeric_choices(self):
        self.assertTrue(InputValidator.validate_numeric_choices("1", 1, 2))
        self.assertTrue(InputValidator.validate_numeric_choices("2", 1, 2))
        self.assertFalse(InputValidator.validate_numeric_choices("3", 1, 2))
        self.assertFalse(InputValidator.validate_numeric_choices("", 1, 5))
        self.assertTrue(InputValidator.validate_numeric_choices("4", 1, 5))
        self.assertFalse(InputValidator.validate_numeric_choices("t", 1, 5))

    def test_validate_string_choices(self):
        self.assertTrue(InputValidator.validate_string_choices("oily", ["Oily", "Normal", "Dry"]))
        self.assertTrue(InputValidator.validate_string_choices("DRY", ["Oily", "Normal", "Dry"]))
        self.assertFalse(InputValidator.validate_string_choices("random", ["Oily", "Normal", "Dry"]))
        self.assertFalse(InputValidator.validate_string_choices("", ["Oily", "Normal", "Dry"]))


if __name__ == '__main__':
    unittest.main()
