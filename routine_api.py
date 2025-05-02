import requests
from products import Product

ENDPOINT = "http://makeup-api.herokuapp.com/api/v1/products.json"

"""

When sending multiple tags in the API call, it only pulls the products which contain all of the tags sent in the call. 
This limits the number of products greatly. Therefore, looping the requests to get products that have at least one of the 
tags will increase the number of recommendations to give to the user. This also complements the scoring system set up in the 
Product class. 

This does, however, create duplication - a product that has an "oil free" tag as well as a "natural" tag will be pulled twice
as two calls are being made. This is dealt with by storing the product ids in the unique_product_ids set. 

"""

# Reusable function that fetches products with given tags, can optionally be given a product type to narrow results
def get_products_by_tags(tags, product_type=None):
    all_api_products = []
    unique_product_ids = set()
    unique_products = []

    # Include tags in the parameters for the request
    for tag in tags:
        try:
            tag_params = {"product_tags": tag}
            if product_type:
                # Add product type to params in provided
                tag_params["product_type"] = product_type

            response = requests.get(url=ENDPOINT, params=tag_params)
            response.raise_for_status()
            data = response.json()
            all_api_products.extend(data)

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")
        except ValueError as json_err:
            print(f"Error decoding JSON: {json_err}")

    # Deduplicate products by ID
    for api_product in all_api_products:
        product_id = api_product.get("id")

        if product_id not in unique_product_ids:
            unique_products.append(api_product)
            unique_product_ids.add(product_id)

    # Creating product objects from Product class and storing the objects in product_list.
    product_list = Product.convert_to_products(unique_products)
    return product_list


def get_skin_type_products(skin_type):
    skin_type_tags = {
        "oily": ["oil free", "hypoallergenic", "natural", "silicone free"],
        "dry": ["alcohol free", "natural", "hypoallergenic", "vegan"],
        "sensitive": ["hypoallergenic", "alcohol free", "natural", "organic"],
        "acne-prone": ["oil free", "hypoallergenic", "silicone free", "alcohol free", "natural", "organic"],
        "combination": ["hypoallergenic", "natural", "oil free", "alcohol free"],
        "normal": ["natural", "vegan", "hypoallergenic"]
    }

    tags = skin_type_tags[skin_type]
    product_list = get_products_by_tags(tags)

    recommended_products = Product.get_skin_recommendations(product_list, skin_type)
    return recommended_products  # returns list of the recommended Product objects


def get_eco_products(product_type):
    eco_conscious_tags = [
        "Fair Trade",
        "Vegan",
        "Cruelty Free",
        "CertClean",
        "Natural",
        "OrganicEcoCert",
        "EWG Verified"
    ]

    return get_products_by_tags(product_type, eco_conscious_tags)


def get_vegan_products(product_type):
    vegan_tags = [
        "Vegan",
        "Cruelty Free",
        "Non-GMO",
    ]

    return get_products_by_tags(product_type, vegan_tags)


def get_natural_products(product_type):
    natural_tags = [
        "Natural",
        "Organic",
        "USDA Organic",
        "EcoCert",
        "Chemical-free",
        "Non-GMO",
        "Purpicks"
    ]

    return get_products_by_tags(product_type, natural_tags)

# print(get_eco_products("eyeliner"))