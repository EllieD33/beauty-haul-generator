import unittest
from unittest.mock import patch, MagicMock

from data.db_utils import insert_new_user_routine, DbConnectionError


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


if __name__ == '__main__':
    unittest.main()
