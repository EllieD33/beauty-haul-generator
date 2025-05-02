import re


class Product:
    def __init__(self, product_id, brand, name, price, description, product_type, tag_list, category, product_colours):
        self.__id = product_id
        self.__brand = brand
        self.__name = name
        self.__price = price
        self.__description = self._extract_first_sentence(description)
        self.__product_type = product_type
        self.__tag_list = tag_list
        self.__category = category
        self.__product_colours = product_colours
        self.__relevance_score = 0

    # Setters
    def set_relevance_score(self, score):
        self.__relevance_score += score

    # Getters
    def get_product_id(self):
        return self.__id


    def get_product_type(self):
        return self.__product_type

    def get_price(self):
        return self.__price

    def get_relevance_score(self):
        return self.__relevance_score

    # helper function to extract first sentence of product description and clean whitespace/line breaks.
    @staticmethod
    def _extract_first_sentence(text):
        clean_text = re.sub(r"\s+", " ", text).strip()

        temp_text = clean_text
        replacements = {
            "Dr.": "dr_PLACEHOLDER",
            "e.l.f.": "elf_PLACEHOLDER"
        }

        for original, placeholder in replacements.items():
            temp_text = temp_text.replace(original, placeholder)

        parts = temp_text.split(".", 1)
        first_sentence = parts[0] + "." if len(parts) > 1 else clean_text

        for original, placeholder in replacements.items():
            first_sentence = first_sentence.replace(placeholder, original)

        return first_sentence

    def display_info(self):
        print(f"🧴 Product: {self.__name} by {self.__brand}")
        price = float(self.__price)
        print(f"💰 Price: £{price:.2f}")
        print(f"📂 Type: {self.__product_type}")
        print(f"📝 Description: {self.__description[:150] + "..." if len(self.__description) > 150 else self.__description}\n")

    # method gets called in get_skin_recommendations() for each product in list.
    def get_skin_compatibility(self, skin_type):
        tags = [tag.lower().strip() for tag in self.__tag_list]

        skin_type_tags = {
            "oily": ["oil free", "hypoallergenic", "natural", "silicone free"],
            "dry": ["alcohol free", "natural", "hypoallergenic", "vegan"],
            "sensitive": ["hypoallergenic", "alcohol free", "natural", "organic"],
            "acne-prone": ["oil free", "hypoallergenic", "silicone free", "alcohol free", "natural", "organic"],
            "combination": ["hypoallergenic", "natural", "oil free", "alcohol free"],
            "normal": ["natural", "vegan", "hypoallergenic"]
        }

        skin_compatibility_score = 0

        for tag in tags:
            if tag in skin_type_tags[skin_type.lower().strip()]:
                skin_compatibility_score += 1

        self.set_relevance_score(skin_compatibility_score)
        return skin_compatibility_score

    # method takes list of products and  skin_type (user input will determine skin type)
    @staticmethod
    def get_skin_recommendations(products, skin_type):
        scored_products = []
        for product in products:
            product.get_skin_compatibility(skin_type)
            if product.get_relevance_score() > 0:
                scored_products.append(product)

        if not scored_products:
            return []

        scored_products.sort(key=lambda p: p.get_relevance_score(), reverse=True)
        return scored_products

    # this method converts API data to list of product objects
    @staticmethod
    def convert_to_products(data):

        product_object_list = []

        for item in data:
            product_id = item.get("id")
            brand = item.get("brand")
            name = item.get("name")
            price = item.get("price")
            description = item.get("description")
            product_type = item.get("product_type")
            tag_list = item.get("tag_list", [])
            category = item.get("category")
            product_colours = item.get("product_colors", [])

            product_object = Product(
                product_id=product_id,
                brand=brand,
                name=name,
                price=price,
                description=description,
                product_type=product_type,
                tag_list=tag_list,
                category=category,
                product_colours=product_colours
            )

            product_object_list.append(product_object)

        return product_object_list

    # this method converts the product data into a dictionary
    def routine_to_dict(self):
        return {
            "Brand": self.__brand,
            "Product": self.__name,
            "Price": self.__price,
            "Description": self.__description,
            "Score": self.__relevance_score
        }


if __name__ == "__main__":
    pass
