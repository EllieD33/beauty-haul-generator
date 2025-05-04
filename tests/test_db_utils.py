import unittest
from unittest.mock import patch, MagicMock
import csv
import os

from data.db_utils import insert_new_user_routine, DbConnectionError
from core.routine_display import SaveRoutine

class MockProduct:
    def __init__(self, brand, product, price, desc, score):
        self.brand = brand
        self.product = product
        self.price = price
        self.desc = desc
        self.score = score

    def routine_to_dict(self):
        return {
            'Brand': self.brand,
            'Product': self.product,
            'Price': self.price,
            'Description': self.desc,
            'Score': self.score
        }


class TestInsertNewUserRoutine(unittest.TestCase):

    @patch('data.db_utils._connect_to_db')
    def test_insert_new_user_routine_success(self, mock_connect):
        # Mock routine
        mock_routine = [
            MockProduct('deciem', 'Serum Foundation', 6.7, 'Lightweight serum', 2),
            MockProduct('pacifica', 'Eye Pencil', 16.0, 'Smooth waterproof', 2)
        ]

        # Mock db connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.lastrowid = 42
        mock_connect.return_value = mock_conn

        # Call the function
        insert_new_user_routine(mock_routine)

        # Assert insert into user_routines was called
        mock_cursor.execute.assert_any_call("INSERT INTO user_routines (user_id) VALUES (1)")

        # Assert at least one product insert happened
        self.assertGreaterEqual(mock_cursor.execute.call_count, 3)  # 1 for routine + 2 for products = 3

        # Ensure commit and close
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('data.db_utils._connect_to_db', side_effect=Exception("Connection failed"))
    def test_insert_new_user_routine_failure(self, mock_connect):
        with self.assertRaises(DbConnectionError):
            insert_new_user_routine([])


class TestSavingToCSV(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_db_to_csv"
        self.fullpath = f"user_routines/{self.test_file}.csv"
        self.test_data_dicts = [
            {"Brand": "Fenty", "Product": "Foundation", "Price": "30", "Description": "Test description", "Score": 4},
            {"Brand": "MAC", "Product": "Lipstick", "Price": "19.99", "Description": "MAC Ruby Woo Lipstick",
             "Score": 8}]


    def test_save_to_csv(self):
        routine_saver = SaveRoutine(self.test_data_dicts, self.test_file)
        routine_saver.save_to_csv(self.test_data_dicts)
        try:
            with open(self.fullpath, "r") as csv_file:
                reader = csv.DictReader(csv_file)
                rows = list(reader)
                for row in rows:
                    print(row)
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["Product"], "Foundation")
            self.assertEqual(rows[1]["Price"], "19.99")
        except FileNotFoundError:
            print("❌ Could not open the file, file doesn't exist")

    def tearDown(self):
        if os.path.exists(self.fullpath):
            os.remove(self.fullpath)
            print("Test file removed ✅")
        else:
            print("No test file found, no removal needed")



if __name__ == '__main__':
    unittest.main()

