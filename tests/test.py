# File for unit tests.
import unittest

from user_input import InputValidator


class TestInputValidator(unittest.TestCase):
    def test_validate_yes_no(self):
        self.assertTrue(InputValidator.validate_yes_no("Y"))
        self.assertTrue(InputValidator.validate_yes_no("n"))
        self.assertFalse(InputValidator.validate_yes_no("yes"))
        self.assertFalse(InputValidator.validate_yes_no("No"))
        self.assertFalse(InputValidator.validate_yes_no(""))

if __name__ == '__main__':
    unittest.main()
