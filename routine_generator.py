from filters import AdvancedFilter
from routine_api import get_skin_type_products


class RoutineGenerator:
    def __init__(self, user_responses):
        self.user_responses = user_responses

    def generate_routine(self):
        # Get products for the user's skin-type
        product_list = get_skin_type_products(self.user_responses["skin_type"])
        routine_filter = AdvancedFilter

        # Remove product types the user has not specified as part of their routine
        relevant_products = routine_filter.filter_product_types(self.user_responses["product_types"], product_list)

        refined_product_list = []

        # Apply advanced filtering for each product type user wants in their routine
        for product_type in self.user_responses["product_types"]:
            filtered_products = routine_filter.filter_by_relevance(
                self.user_responses["priorities"], product_type, self.user_responses["budget"], relevant_products
            )

            # Add the filtered products to the refined list
            refined_product_list.extend(filtered_products)

        # Ensure no duplicates
        refined_product_list = list(set(refined_product_list))

        return refined_product_list
