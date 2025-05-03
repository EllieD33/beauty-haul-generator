class UserPreferences:
    def __init__(self):
        self.__skin_type = None
        self.__budget = None
        self.__product_types = None
        self.__priorities = None

    # Setter methods

    def set_skin_type(self, skin_type):
        self.__skin_type = skin_type.lower()

    def set_budget(self, budget):
        self.__budget = budget

    def set_product_type(self, product_types):
        self.__product_types = product_types

    def set_priorities(self, priorities):
        self.__priorities = priorities

    # Getter methods
    def get_skin_type(self):
        return self.__skin_type

    def get_budget(self):
        return self.__budget

    def get_product_preference(self):
        return self.__product_types

    def get_priorities(self):
        return self.__priorities

    def preferences_to_dict(self):
        return {
            "skin_type": self.__skin_type,
            "budget": self.__budget,
            "product_types": self.__product_types,
            "priorities": self.__priorities
        }


if __name__ == "__main__":
    pass
