from enum import Enum
from Enums.SideDishPrices import SideDishPrices
from MenuItem import MenuItem


# SideDish class Represents different the diners SideDish
class SideDish(MenuItem):
    def __init__(self, i_diner_name: str, i_side_dish_type: Enum):
        super().__init__(i_diner_name, i_side_dish_type)
        # Checking meal item's type and validation
        if i_side_dish_type == SideDishPrices.three_cheese_asparagus_gratin:
            self.__m_price = int(SideDishPrices.three_cheese_asparagus_gratin.value)
            self.__m_side_dish_type: SideDishPrices = SideDishPrices.three_cheese_asparagus_gratin
        elif i_side_dish_type == SideDishPrices.corn_pudding:
            self.__m_price = int(SideDishPrices.corn_pudding.value)
            self.__m_side_dish_type: SideDishPrices = SideDishPrices.corn_pudding
        elif i_side_dish_type == SideDishPrices.chips:
            self.__m_price = int(SideDishPrices.chips.value)
            self.__m_side_dish_type: SideDishPrices = SideDishPrices.chips
        else:
            print("The dish you want is not in the menu today")

    # Gets SideDish Meal prices
    def get_side_dish_price(self) -> int:
        return self.__m_price
