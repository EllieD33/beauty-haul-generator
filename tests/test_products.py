import unittest
from products import Product

class TestProducts(unittest.TestCase):
    def setUp(self):

        self.product = Product(
            product_id="111",
            brand="Test Brand",
            name="Test Product",
            price="20.99",
            description="This is a test product. The first test product.",
            tag_list=["Vegan"],
            product_type="Test type",
            category="Test category",
            product_colours=[{"hex_value": "#E1BFC0", "colour_name": "this is a test colour"}],
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
            brand="Test Another Brand Again. This time it's e.l.f.",
            name="Test Another Product Again",
            price="10.99",
            description="You'll like this e.l.f. brand.",
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

    # Test the getter methods
    def test_get_product_id(self):
        self.assertEqual(self.product.get_product_id(), "111")

    def test_get_product_type(self):
        self.assertEqual(self.product2.get_product_type(), "Test type")

    def test_get_price(self):
        self.assertEqual(self.product3.get_price(), "10.99")


    # Testing helper method _extract_first_sentence
    def test_extract_first_sentence(self):
        # Testing just first sentence pulled
        description_product = getattr(self.product, "_Product__description")
        self.assertEqual(description_product, "This is a test product.")

        # Testing full description extracted if no full stop
        description_product2 = getattr(self.product2, "_Product__description")
        self.assertEqual(description_product2, "This is another test product for you")

        # Testing abbreviation does not affect sentence extraction.
        description_product3 = getattr(self.product3, "_Product__description")
        self.assertEqual(description_product3, "You'll like this e.l.f. brand.")


    # Test get_skin_compatibility()
    def test_get_skin_compatibility(self):
        self.assertEqual(self.product.get_skin_compatibility("oily"), 0) # Testing no tags met
        self.assertEqual(self.product2.get_skin_compatibility("oily"), 2) # Testing some tags met
        self.assertEqual(self.product3.get_skin_compatibility("oily"), 4) # Testing all tags met
        self.assertEqual(self.product4.get_skin_compatibility("oily"), 0) # Testing empty list

        self.assertEqual(self.product.get_skin_compatibility("DRY"), 1)  # Testing capitals
        self.assertEqual(self.product.get_skin_compatibility("   dry   "), 1)  # Testing whitespace


    # Test get_skin_recommendations()
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