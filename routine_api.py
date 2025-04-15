import requests
from products import Product

ENDPOINT = "http://makeup-api.herokuapp.com/api/v1/products.json"

def get_all_products():
    response = requests.get(url=ENDPOINT)
    response.raise_for_status()
    data = response.json()
    return data

def get_products_by_brand(brand):
    brand_params = {"brand": brand}
    response = requests.get(url=ENDPOINT, params=brand_params)
    response.raise_for_status()
    data = response.json()
    return data

def get_products_by_type(type):
    pass

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
    unique_products = {}

    all_api_products = []
    for tag in tags:
        tag_params = {"product_tags": tag}
        response = requests.get(url=ENDPOINT, params=tag_params)
        response.raise_for_status()
        data = response.json()
        all_api_products.extend(data)

    for api_product in all_api_products:
        product_id = api_product.get("id")

        if product_id not in unique_products:
            product = Product(
                product_id=product_id,
                brand=api_product.get("brand"),
                name=api_product.get("name"),
                price=api_product.get("price"),
                description=api_product.get("description"),
                product_type=api_product.get("product_type"),
                tag_list=api_product.get("tag_list", []),
                category=api_product.get("category"),
                product_colours=api_product.get("product_colours", [])
            )
            unique_products[product_id] = product

    product_list = list(unique_products.values())

    recommended_products = Product.get_skin_recommendations(product_list, skin_type, limit)

    return recommended_products

# FOR FRONTEND - just testing here
user_recs = (get_skin_type_products("acne-prone", 10))

print("RECOMMENDED PRODUCTS: ")
for product, score in user_recs:
    product.display_info()
    print(f"Compatibility score: {score}\n")
