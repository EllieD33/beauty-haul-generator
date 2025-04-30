from routine_api import get_vegan_products, get_natural_products, get_eco_products


class AdvancedFilter:
    @staticmethod
    def apply_budget(budget_key, products):
        # Defining the budget values for each category
        budget_map = {
            "£": 20.00,
            "££": 30.00,
            "£££": 40.00,
            "££££": float('inf')  # No limit (infinite)
        }
        budget = budget_map.get(budget_key, float('inf'))  # Infinite set as fallback value
        return [product for product in products if float(product.get_price()) <= budget]

    @staticmethod
    def filter_product_types(desired_product_types, products):
        return [product for product in products if
                product.get_product_type().lower() in (p.lower() for p in desired_product_types)]

    @staticmethod
    def filter_by_relevance(priorities, product_type, budget, products):
        try:
            priority_function_map = {
                "1": lambda b, p: AdvancedFilter.apply_budget(b, p),
                "2": get_vegan_products,
                "3": get_eco_products,
                "4": get_natural_products
            }

            # Points to be added to product relevance score: higher priority gives higher points
            priority_score_map = {
                "1": 4,
                "2": 3,
                "3": 2,
                "4": 1
            }

            all_filtered_products = products

            for rank in priorities:
                if rank == "1":
                    api_filtered_products = priority_function_map[rank](budget, all_filtered_products)

                else:
                    api_filtered_products = priority_function_map[rank](product_type)

                # Filter the original products by product type
                filtered_products_by_type = AdvancedFilter.filter_product_types(product_type, all_filtered_products)

                # Compare the filtered products by type with the API results
                acceptable_products = AdvancedFilter.compare_products(api_filtered_products, filtered_products_by_type)

                # If no products match, return the previously filtered results (we don't want to remove all products)
                if not acceptable_products:
                    return all_filtered_products

                # Add score to relevance based on priority rank
                score_to_add = priority_score_map.get(rank, 0)
                for product in acceptable_products:
                    product.add_relevance_score(score_to_add)

                # Update the list of products for the next priority
                all_filtered_products = acceptable_products

                if len(all_filtered_products) <= 1:
                    return all_filtered_products

            # Return the final list of filtered products
            return all_filtered_products

        except Exception as e:
            print(f"⚠️ Error in filter_by_relevance: {e}")
            return products # return unfiltered list

    @staticmethod
    def compare_products(api_products, provided_products):
        # Create a set of product IDs from the API products
        api_product_ids = {product.get_product_id() for product in api_products}

        # Filter the provided products to find matching products
        acceptable_products = [product for product in provided_products if product.get_product_id() in api_product_ids]

        return acceptable_products
