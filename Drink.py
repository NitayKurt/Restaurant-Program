from enum import Enum
from Enums.DrinkPrices import DrinkPrices
from MenuItem import MenuItem


# Drink class Represents different the diners Drink
class Drink(MenuItem):
    # Checking meal item's type and validation
    def __init__(self, i_diner_name: str, i_drink_type: Enum):
        super().__init__(i_diner_name, i_drink_type)
        if i_drink_type == DrinkPrices.water:
            self.__m_price = int(DrinkPrices.water.value)
            self.__m_drink_type = DrinkPrices.water
        elif i_drink_type == DrinkPrices.Coca_Cola:
            self.__m_price = int(DrinkPrices.Coca_Cola.value)
            self.__m_drink_type = DrinkPrices.Coca_Cola
        elif i_drink_type == DrinkPrices.FuzeTea:
            self.__m_price = int(DrinkPrices.FuzeTea.value)
            self.__m_drink_type = DrinkPrices.FuzeTea
        elif i_drink_type == DrinkPrices.Orange_Juice:
            self.__m_price = int(DrinkPrices.Orange_Juice.value)
            self.__m_drink_type = DrinkPrices.Orange_Juice
        else:
            print("The dish you want is not in the menu today")

    # Gets Drink prices
    def get_drink_price(self) -> int:
        return self.__m_price
