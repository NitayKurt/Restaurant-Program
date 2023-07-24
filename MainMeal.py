from enum import Enum
from Enums.MainMealPrices import MainMealPrices
from MenuItem import MenuItem


# Main Meal class Represents different the diners main meal
class MainMeal(MenuItem):
    # Checks the type of the meal
    def __init__(self, i_diner_name: str, i_meal_type: Enum):
        super().__init__(i_diner_name, i_meal_type)
        if i_meal_type == MainMealPrices.soup:
            self.__m_price = int(MainMealPrices.soup.value)
            self.__m_meal_type = MainMealPrices.soup
        elif i_meal_type == MainMealPrices.Shakshuka:
            self.__m_price = int(MainMealPrices.Shakshuka.value)
            self.__m_meal_type = MainMealPrices.Shakshuka.value
        elif i_meal_type == MainMealPrices.Fish_and_chips:
            self.__m_price = int(MainMealPrices.Fish_and_chips.value)
            self.__m_meal_type = MainMealPrices.Fish_and_chips.value
        elif i_meal_type == MainMealPrices.Lazania:
            self.__m_price = int(MainMealPrices.Lazania.value)
            self.__m_meal_type = MainMealPrices.Lazania.value
        else:
            print("The dish you want is not in the menu today")

    # Gets Main Meal prices
    def get_main_meal_price(self) -> int:
        return self.__m_price
