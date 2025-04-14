class Product:
    def __init__(self, product_id, brand, name, price, description, product_type, tag_list, category, product_colours):
        self.__id = product_id
        self.__brand = brand
        self.__name = name
        self.__price = price
        self.__description = description
        self.__product_type = product_type
        self.__tag_list = tag_list
        self.__category = category
        self.__product_colours = product_colours

    # getter
    def get_name(self):
        return self.__name

    # getter
    def display_info(self):
        print(f"Brand: {self.__brand}, Product: {self.__name} ({self.__product_type})\n"
              f"Price: {self.__price}\n"
              f"Description: {self.__description}")

    # this function gets called in static method for each product in list.
    def get_skin_compatibility(self, skin_type):
        tags = [tag.lower() for tag in self.__tag_list]

        skin_type_tags = {
            "oily": ["oil free", "hypoallergenic", "natural", "silicone free"],
            "dry": ["alcohol free", "natural", "hypoallergenic", "vegan"],
            "sensitive": ["hypoallergenic", "alcohol free", "natural"],
            "acne-prone": ["oil free", "hypoallergenic", "silicone free", "alcohol free", "natural"],
            "combination": ["hypoallergenic", "natural", "oil free", "alcohol free"],
            "normal": ["natural", "vegan", "hypoallergenic"]
        }

        skin_compatibility_score = 0

        for tag in tags:
            if tag in skin_type_tags[skin_type.lower()]:
                skin_compatibility_score += 1

        return skin_compatibility_score

    # method takes list of products, skin_type, and limit number of products to be recommended (user input will determine skin type and limit)
    @staticmethod
    def get_skin_recommendations(products, skin_type, limit):
        product_scores = {}
        for product in products:
            score = product.get_skin_compatibility(skin_type)
            if score > 0:
                product_scores[product] = score

        if not product_scores:
            print("No suitable products found")
            return []


        product_recommendations = sorted(product_scores.items(), key=lambda x: x[1], reverse=True)

        return product_recommendations[:limit]

# refine below (testing to see everything works)
product1 = Product("12", "BrandA", "PRoductA", "20.00", "Sample product", "Foundation", ["hypoallergenic"], "powder", "brown")
product2 = Product("124", "BrandB", "PRoductB", "10.00", "Sample product", "Lipstick", ["oil free", "vegan", "alcohol free"], "liquid", "pink")
prods = [product1, product2]

# similar implementation to be used in frontend
all_recs = Product.get_skin_recommendations(prods, "dry", len(prods))
for product, score in all_recs:
    print(f"Product: {product.get_name()}, score: {score}")

if __name__ == "__main__":
    pass