import unittest
from products import Product

class TestProducts(unittest.TestCase):
    def setUp(self):

        self.product = Product(
            product_id="111",
            brand="Test Brand",
            name="Test Product",
            price="20.99",
            description="This is a test product",
            tag_list=["Vegan"],
            product_type="Test type",
            category="Test category",
            product_colours=[{"hex_value": "#E1BFC0", "colour_name": "this is a test colour"}]
        )

        # Additional products for recommendation tests
        self.product2 = Product(
            product_id="222",
            brand="Test Another Brand",
            name="Test Another Product",
            price="30.99",
            description="This is another test product for you",
            tag_list=["Oil free", "Alcohol free", "Natural"],
            product_type="Test type",
            category="Test category",
            product_colours=[{"hex_value": "#E1BFC6", "colour_name": "this is another test colour"}]
        )

        self.product3 = Product(
            product_id="333",
            brand="Test Another Brand Again",
            name="Test Another Product Again",
            price="10.99",
            description="This is a third test product for you",
            tag_list=["Oil free", "Alcohol free", "Natural", "Hypoallergenic", "Silicone free", "Vegan"],
            product_type="Test type",
            category="Test category",
            product_colours=[{"hex_value": "#E1BFC9", "colour_name": "this is a third test colour"}]
        )

        self.product4 = Product(
            product_id="444",
            brand="Test Another Brand Again 4",
            name="Test Another Product Again 4",
            price="10.99",
            description="This is a 4th test product for you",
            tag_list=[],
            product_type="Test type",
            category="Test category",
            product_colours=[{"hex_value": "#E1BFC9", "colour_name": "this is a third test colour"}]
        )

    # Test the get_name() method
    def test_get_name(self):
        self.assertEqual(self.product.get_name(), "Test Product")

    # Test check_suitable_for_skin_type method for oily skin
    def test_get_skin_compatibility(self):
        self.assertEqual(self.product.get_skin_compatibility("oily"), 0) # Testing no tags met
        self.assertEqual(self.product2.get_skin_compatibility("oily"), 2) # Testing some tags met
        self.assertEqual(self.product3.get_skin_compatibility("oily"), 4) # Testing all tags met
        self.assertEqual(self.product4.get_skin_compatibility("oily"), 0) # Testing empty list

        self.assertEqual(self.product.get_skin_compatibility("DRY"), 1)  # Testing capitals
        self.assertEqual(self.product.get_skin_compatibility("  dry  "), 1)  # Testing whitespace

    def test_get_skin_recommendations(self):
        prod_list = [self.product, self.product2, self.product3, self.product4]
        recommendations = Product.get_skin_recommendations(prod_list, "sensitive")

        self.assertEqual(len(recommendations), 2) # Testing correct number of recs returned.

    def test_get_skin_recommendations_empty(self):
        prod_list = []
        recommendations = Product.get_skin_recommendations(prod_list, "sensitive")
        self.assertEqual(len(recommendations), 0) # Testing if 0 recommendations when given empty list

    def test_get_skin_recommendations_no_match(self):
        prod_list = [self.product, self.product4]
        recommendations = Product.get_skin_recommendations(prod_list, "oily")
        self.assertEqual(len(recommendations), 0)


if __name__ == "__main__":
    unittest.main()