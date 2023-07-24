from enum import Enum
from Enums.StartPrices import StartPrices
from MenuItem import MenuItem


# Starting Meal class Represents different the diners Starting Meal
class StartMeal(MenuItem):
    def __init__(self, i_diner_name: str, i_start_meal_type: Enum):
        super().__init__(i_diner_name)
        # Checking meal item's type and validation
        if i_start_meal_type == StartPrices.Scramble_egg_with_bread:
            self.__m_price = int(StartPrices.Scramble_egg_with_bread)
            self.__m_start_meal_type = StartPrices.Scramble_egg_with_bread
        elif i_start_meal_type == StartPrices.Sandwich_with_Tuna:
            self.__m_price = int(StartPrices.Sandwich_with_Tuna)
            self.__m_start_meal_type = StartPrices.Sandwich_with_Tuna
        elif i_start_meal_type == StartPrices.Salad_with_vegetables:
            self.__m_price = int(StartPrices.Salad_with_vegetables)
            self.__m_start_meal_type = StartPrices.Salad_with_vegetables
        elif i_start_meal_type == StartPrices.Hot_bread_with_butter:
            self.__m_price = int(StartPrices.Hot_bread_with_butter)
            self.__m_start_meal_type = StartPrices.Hot_bread_with_butter
        else:
            print("The dish you want is not in the menu today")

    # Gets Starting Meal prices
    def get_start_meal_price(self) -> int:
        return self.__m_price
