from abc import ABC, abstractmethod
from RestaurantLogic import Table
from Client.Diner import Diner
from Staff.Employee import Employee
from DM.MenuItem import MenuItem
from RestaurantLogic.Table import Table as Table
from UI.ColorPrint import print_cyan, pr_red
from UI.ColorPrint import print_cyan_end

# Interface Class for everyone how can serve tables and clients in the restaurant
class ITableServing(ABC):
    # A method for everyone how can take an order in the restaurant
    @abstractmethod
    def take_orders(self):
        pass

    # A method for everyone how can cancel an order in the restaurant
    @abstractmethod
    # def cancel_order(self, i_client: Diner, i_dish: MenuItem):
    def cancel_order(self):
        pass

    # A method for everyone how can bind client clients to tables in the restaurant
    @abstractmethod
    def add_clients_to_table(self, i_tables):
        pass

    # A method for everyone how can remove clients from tables in the restaurant
    @abstractmethod
    # def remove_client_from_table(self, number_of_a_table: int, restaurant_tables: list[Table], clients: list[Table]):
    def remove_client_from_table(self, restaurant_tables: list[Table]):
        pass

    # A method for everyone how can take an order in the restaurant
    @abstractmethod
    def clean_table(self):
        pass

    # A method for everyone how can search for a diner/client in the restaurant
    @abstractmethod
    def search_for_diner(self, i_restaurant_tables: list[Table]) -> Diner:
      pass



