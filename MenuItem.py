from datetime import datetime
from abc import ABC, abstractmethod
from enum import Enum


# Dessert class Represents different the diners dessert
class MenuItem(ABC):
    # Checking meal item's type and validation
    # def __init__(self, i_diner_name: str, i_type: Enum, i_price: int):
    def __init__(self, i_diner_name: str, i_type: Enum):
        self.__m_item_id = 0
        self.__m_string_time_of_the_order = None
        self.__m_diner_name = i_diner_name
        self._m_item_type = i_type

    # A method that sets the time of the order
    def set_now_as_the_time_for_order(self) -> None:
        self.__m_string_time_of_the_order = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Gets  meal diners name
    def get_diners_name(self) -> str:
        return self.__m_diner_name

    # Gets  meal's type
    def get_item_type(self) -> Enum:
        return self._m_item_type


