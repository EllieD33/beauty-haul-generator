from routine_api import get_vegan_products, get_natural_products, get_eco_products


class AdvancedFilter:
    @staticmethod
    def apply_budget(budget_key, products):
        """
        Filters products based on the user's budget selection.
        """
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
        """
        Filters products based on the user's desired product types.
        """
        return [product for product in products if
                product.get_product_type().lower() in (p.lower() for p in desired_product_types)]

    @staticmethod
    def filter_by_relevance(priorities, product_type, budget, products):
        """
        Filters and scores products based on multiple user-defined priorities.
        """
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
            try:
                if rank == "1":
                    api_filtered_products = priority_function_map[rank](budget, all_filtered_products)

                else:
                    api_filtered_products = priority_function_map[rank](product_type)

                # Compare the filtered products by type with the API results
                acceptable_products = AdvancedFilter.compare_products(api_filtered_products, all_filtered_products)

                # If no products match, return the previously filtered results (we don't want to remove all products)
                if not acceptable_products:
                    continue

                # Add score to relevance based on priority rank
                score_to_add = priority_score_map.get(rank, 0)
                for product in acceptable_products:
                    product.set_relevance_score(score_to_add)

                # Update the list of products for the next priority
                all_filtered_products = acceptable_products

                if len(all_filtered_products) <= 1:
                    break

            except (KeyError, TypeError, AttributeError) as e:
                print(f"\n⚠️ Priority '{rank}' caused an error: {type(e).__name__} - {e}")
                continue # skip this priority but don't exit filtering

        # Return the final list of filtered products
        return all_filtered_products

    @staticmethod
    def compare_products(api_products, provided_products):
        """
        Compares two sets of products and returns only those that appear in both lists based on product ID.
        """
        # Create a set of product IDs from the API products
        api_product_ids = {product.get_product_id() for product in api_products}

        # Filter the provided products to find matching products
        acceptable_products = [product for product in provided_products if product.get_product_id() in api_product_ids]

        return acceptable_products
