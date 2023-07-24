from enum import Enum
from Enums.DessertPrices import DessertPrices
from MenuItem import MenuItem


# Dessert class Represents different the diners dessert
class Dessert(MenuItem):
    # Checks the type of the Dessert
    def __init__(self, i_diner_name: str, i_dessert_type: Enum):
        super().__init__(i_diner_name, i_dessert_type)
        if i_dessert_type == DessertPrices.chocolate_chip_cookies:
            self.__m_price = int(DessertPrices.chocolate_chip_cookies.value)
            self.__m_dessert_type = DessertPrices.chocolate_chip_cookies
        elif i_dessert_type == DessertPrices.apple_pie:
            self.__m_price = int(DessertPrices.apple_pie.value)
            self.__m_dessert_type = DessertPrices.apple_pie
        elif i_dessert_type == DessertPrices.cheese_cake:
            self.__m_price = int(DessertPrices.cheese_cake.value)
            self.__m_dessert_type = DessertPrices.cheese_cake
        else:
            print("The dish you want is not in the menu today")

    # Gets Dessert prices
    def get_dessert_price(self) -> int:
        return self.__m_price

