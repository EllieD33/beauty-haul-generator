class UserPreferences:
    def __init__(self):
        self.__skin_type = None
        self.__budget = None
        self.__product_type = None
        self.__brand_preference = []

    # Setter methods

    def set_skin_type(self, skin_type):
        skin_types = ["dry", "oily", "combination", "normal", "sensitive"]
        if skin_type.lower() in skin_types:
            self.__skin_type = skin_type.lower()
            return True
        return False

    def set_budget(self, budget):
        budgets = ["£", "££", "£££", "££££"]
        if budget in budgets:
            self.__budget = budget
            return True
        return False

    def set_product_type(self, product_types):
        self.__product_type = product_types
        return True

    def add_brand_preference(self, brand):
        brands = ["Almay", "Alva", "Anna Sui", "Annabelle", "Benefit", "Boosh", "Burt's Bees", "Butter London",
                  "C'est Moi", "Cargo Cosmetics", "China Glaze", "Clinique", "Coastal Classic Creation", "Colourpop",
                  "Covergirl", "Danish", "Deciem", "Dior", "Dr. Hauschka", "E.L.F", "Essie", "Fenty", "Glossier",
                  "Green People", "Iman", "L'Oreal", "Lotus Cosmetics", "Maia's Mineral Galaxy", "Marcelle",
                  "Marienatie", "Maybelline", "Milani", "Mineral Fusion", "Misa", "Mistura", "Moov", "Nudus", "Nyx",
                  "Orly", "Pacifica", "Penny Lane Organics", "Physicians Formula", "Piggy Paint", "Pure Anada",
                  "Rejuva Minerals", "Revlon", "Sally B's Skin Yummies", "Salon Perfect", "Sante", "Sinful Colours",
                  "Smashbox", "Stila", "Suncoat", "W3llpeople", "Wet n Wild", "Zorah", "Zorah Biocosmetiques"]
        brand_match = next((b for b in brands if b.lower() == brand.lower()), None)
        if brand_match and brand_match not in self.__brand_preference:
            self.__brand_preference.append(brand_match)
            return True
        return False

    # Getter methods

    def get_skin_type(self):
        return self.__skin_type

    def get_budget(self):
        return self.__budget

    def get_product_preference(self):
        return self.__product_type

    def get_brand_preference(self):
        return self.__brand_preference



if __name__ == "__main__":
    pass