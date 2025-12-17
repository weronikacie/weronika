from magazine import utils

class Product:
    def __init__(self, name):
        self.name = name
        print(f"Stworzono produkt: {self.name}")
        print(utils.helper_function())