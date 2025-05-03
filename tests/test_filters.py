import unittest
from unittest.mock import MagicMock

from filters import AdvancedFilter


class TestAdvancedFilter(unittest.TestCase):

    def test_compare_products(self):
        # Mock products
        mock_product_1 = MagicMock()
        mock_product_1.get_product_id.return_value = "product_1"

        mock_product_2 = MagicMock()
        mock_product_2.get_product_id.return_value = "product_2"

        mock_product_3 = MagicMock()
        mock_product_3.get_product_id.return_value = "product_3"

        # Set up inputs
        api_products = [mock_product_1, mock_product_2]
        provided_products = [mock_product_1, mock_product_3]

        # Call the method
        result = AdvancedFilter.compare_products(api_products, provided_products)

        # Assert that only product_1 is returned (it's the only one that exists in both lists)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], mock_product_1)

        # Assert that the returned product has the expected ID
        self.assertEqual(result[0].get_product_id(), "product_1")

    def test_filter_product_types(self):
        # Mock products
        product1 = MagicMock()
        product1.get_product_type.return_value = "lipstick"

        product2 = MagicMock()
        product2.get_product_type.return_value = "foundation"

        product3 = MagicMock()
        product3.get_product_type.return_value = "mascara"

        # Set up inputs
        desired_types = ["lipstick", "mascara"]
        products = [product1, product2, product3]

        # Call the method
        result = AdvancedFilter.filter_product_types(desired_types, products)

        # Only products with matching types are returned
        self.assertEqual(result, [product1, product3])

    def test_apply_budget(self):
        # Mock the products and returned values
        product1 = MagicMock()
        product1.get_price.return_value = "10.00"

        product2 = MagicMock()
        product2.get_price.return_value = "25.00"

        product3 = MagicMock()
        product3.get_price.return_value = "35.00"

        product4 = MagicMock()
        product4.get_price.return_value = "50.00"

        products = [product1, product2, product3, product4]

        # Test with budget "£" (20.00)
        budget_key = "£"
        filtered_products = AdvancedFilter.apply_budget(budget_key, products)
        self.assertEqual(filtered_products, [product1])

        # Test with budget "££" (30.00)
        budget_key = "££"
        filtered_products = AdvancedFilter.apply_budget(budget_key, products)
        self.assertEqual(filtered_products, [product1, product2])

        # Test with budget "£££" (40.00)
        budget_key = "£££"
        filtered_products = AdvancedFilter.apply_budget(budget_key, products)
        self.assertEqual(filtered_products, [product1, product2, product3])

        # Test with budget "££££" (infinite budget)
        budget_key = "££££"
        filtered_products = AdvancedFilter.apply_budget(budget_key, products)
        self.assertEqual(filtered_products, [product1, product2, product3, product4])

        # Test with an invalid budget key (fallback to infinite budget)
        budget_key = "invalid"
        filtered_products = AdvancedFilter.apply_budget(budget_key, products)
        self.assertEqual(filtered_products, [product1, product2, product3, product4])


if __name__ == "__main__":
    unittest.main()
