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


    def display_info(self):
        print(f"Brand: {self.__brand}, Product: {self.__name} ({self.__product_type})\n"
              f"Price: {self.__price}\n"
              f"Description: {self.__description}")


    def check_suitable_for_skin_type(self, skin_type):
        tags = [tag.lower() for tag in self.__tag_list]

        skin_type_tags = {
            "oily": ["oil free", "hypoallergenic", "natural", "silicone free"],
            "dry": ["alcohol free", "natural", "hypoallergenic", "vegan"],
            "sensitive": ["hypoallergenic", "alcohol free", "natural"],
            "acne-prone": ["oil free", "hypoallergenic", "silicone free", "alcohol free", "natural"],
            "combination": ["hypoallergenic", "natural", "oil free", "alcohol free"],
            "normal": ["natural", "vegan", "hypoallergenic"]
        }

        if skin_type.lower() not in skin_type_tags:
            return False

        for skin_type_tag in skin_type_tags[skin_type.lower()]:
            if skin_type_tag in tags:
                return True

        return False

