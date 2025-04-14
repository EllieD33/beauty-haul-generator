import requests

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


