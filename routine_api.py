import requests
from products import Product

ENDPOINT = "http://makeup-api.herokuapp.com/api/v1/products.json"


def get_all_products():
    response = requests.get(url=ENDPOINT)
    response.raise_for_status()
    data = response.json()
    return Product.convert_to_products(data) # returns list of product objects


def get_products_by_brand(brand):
    brand_params = {"brand": brand}
    response = requests.get(url=ENDPOINT, params=brand_params)
    response.raise_for_status()
    data = response.json()
    return Product.convert_to_products(data)


def get_products_by_type(prod_type):
    type_params = {"product_type": prod_type}
    response = requests.get(url=ENDPOINT, params=type_params)
    response.raise_for_status()
    data = response.json()
    return Product.convert_to_products(data)

def get_products_by_price(less_than):
    price_params = {"price_less_than": less_than}
    response = requests.get(url=ENDPOINT, params=price_params)
    response.raise_for_status()
    data = response.json()
    return Product.convert_to_products(data)


"""

When sending multiple tags in the API call, it only pulls the products which contain all of the tags sent in the call. 
This limits the number of products greatly. Therefore, looping the requests to get products that have at least one of the 
tags will increase the number of recommendations to give to the user. This also complements the scoring system set up in the 
Product class. 

This does, however, create duplication - a product that has an "oil free" tag as well as a "natural" tag will be pulled twice
as two calls are being made. This is dealt with by storing the product ids in the unique_product_ids set. 

"""


def get_skin_type_products(skin_type, limit):
    skin_type_tags = {
        "oily": ["oil free", "hypoallergenic", "natural", "silicone free"],
        "dry": ["alcohol free", "natural", "hypoallergenic", "vegan"],
        "sensitive": ["hypoallergenic", "alcohol free", "natural", "organic"],
        "acne-prone": ["oil free", "hypoallergenic", "silicone free", "alcohol free", "natural", "organic"],
        "combination": ["hypoallergenic", "natural", "oil free", "alcohol free"],
        "normal": ["natural", "vegan", "hypoallergenic"]
    }

    tags = skin_type_tags[skin_type]
    all_api_products = []
    unique_product_ids = set()
    unique_products = []

    for tag in tags:
        tag_params = {"product_tags": tag}
        response = requests.get(url=ENDPOINT, params=tag_params)
        response.raise_for_status()
        data = response.json()
        all_api_products.extend(data)

    for api_product in all_api_products:
        product_id = api_product.get("id")

        if product_id not in unique_product_ids:
            unique_products.append(api_product)
            unique_product_ids.add(product_id)

    # Creating product objects from Product class and storing the objects in product_list.
    product_list = Product.convert_to_products(unique_products)

    recommended_products = Product.get_skin_recommendations(product_list, skin_type, limit)

    return recommended_products  # returns list of the recommended Product objects

# FOR FRONTEND - just testing here
# user_recs = get_skin_type_products("normal", 10)
#
# print("RECOMMENDED PRODUCTS: ")
# for product, score in user_recs:
#     product.display_info()
#     print(f"Compatibility score: {score}\n")

# fenty_prods = get_products_by_brand("fenty")
#
# for item in fenty_prods:
#     item.display_info()

# price_prods = get_products_by_price(20)
# for item in price_prods:
#     item.display_info()