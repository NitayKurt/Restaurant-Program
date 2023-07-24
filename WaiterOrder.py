from __future__ import annotations
from typing import TYPE_CHECKING
from IDAO.ITableServing import ITableServing
from DM import MenuItem
from Client.Diner import Diner
from RestaurantLogic.Table import Table as Table
from Enums.DessertPrices import DessertPrices
from Enums.DrinkPrices import DrinkPrices
from Enums.SideDishPrices import SideDishPrices
from Enums.StartPrices import StartPrices
from Enums.MainMealPrices import MainMealPrices
from RestaurantLogic import Restaurant
import time

from UI.ColorPrint import print_cyan, pr_red

from UI.ColorPrint import print_cyan_end

# Mechanism that make a module acknowledge the existence of circular import without the use of them
# Uses the 2 first lines
if TYPE_CHECKING:
    from Staff.Waiter import Waiter


# Waiter Interface implementation. implementing ITableServing Interface
class WaiterOrder(ITableServing):
    self: Waiter

    # Waiter Taking order method (with a couple of checks)
    def take_orders(self: Waiter):
        found_at_least_one_order = False
        table_number = int(input("Enter table you want to take orders from : "))
        table_i_waiter = self.get_tables_i_waiter()
        for table in table_i_waiter:
            if table.get_table_number() == table_number:
                tables_diners = table.get_tables_diners()
                if tables_diners:
                    for client in tables_diners:
                        client_orders = client.get_orders_waiting_list()
                        if client_orders:
                            found_al_least_one_order = True
                            for order in client_orders:
                                if order:
                                    order.set_now_as_the_time_for_order()
                                    for i in range(5):
                                        print_cyan_end(". ")
                                        time.sleep(1)
                                    self.serve_table(table)
                                    break
                                else:
                                    print_cyan(f"Couldn't find any orders in table No. {table_number} ")
                            print_cyan("Waiter took table orders and passed it to the chef\n"
                                       "Waiting for the food to be made")
                        else:
                            pr_red(f"client does not have orders")
                    if not found_at_least_one_order:
                        print_cyan(f"Couldn't find any orders in table No. {table_number} ")
                else:
                    print_cyan(f"Couldn't find any diners in table No. {table_number} ")
            break
        else:
            print_cyan(f"Couldn't find table No. {table_number} ")

    # Waiter Cancel order method (with a couple of checks)
    def cancel_order(self: Waiter):
        client_name = input("Enter client name you want to cancel orders to : ")
        dish_name = input("Enter dish's name to cancel: ")
        if self.is_valid_order(dish_name):
            for table in self.get_tables_i_waiter():
                table_diners = table.get_tables_diners()
                if table_diners:
                    for diner in table.get_tables_diners():
                        if diner.get_name() == client_name:
                            order: MenuItem
                            orders = diner.get_orders_waiting_list()
                            if orders:
                                for order in orders:
                                    if order.get_name() == dish_name:
                                        print_cyan(f"Order {order.get_name()} cancelled")
                                        del order
                                        break
                    else:
                        print_cyan("I'm sorry im not you waiter i cant cancel orders for you")
                else:
                    print_cyan(f"Couldn't find diners in the table No. {table.get_table_number()}")
        else:
            print_cyan(f"The {dish_name} is not a valid order")

    # Waiter Method that checks if an order is valid
    @staticmethod
    def is_valid_order(dish_name):
        for e in DrinkPrices:
            if e.name is dish_name:
                return True
        for e in SideDishPrices:
            if e.name == dish_name:
                return True
        for e in StartPrices:
            if e.name is dish_name:
                return True
        for e in DessertPrices:
            if e.name == dish_name:
                return True
        for e in MainMealPrices:
            if e.name == dish_name:
                return True
        return False

    # Waiter method that adds client to restaurant
    def new_restaurant_client(self: Waiter, i_restaurant_tables):
        number_of_clients = int(input("Enter the number of diners for the tables : "))
        print_cyan(number_of_clients)
        list_of_new_diners: list[Diner] = list()
        for index in range(number_of_clients):
            client_name = input("Enter the diner's name : ")
            print_cyan(client_name)
            list_of_new_diners.append(Diner(client_name))
        # self.waiter.search_table_for_new_diners(i_restaurant_tables, list_of_new_diners)
        self.search_table_for_new_diners(i_restaurant_tables, list_of_new_diners)

    # Waiter method that search's a empty table for a new customer
    @staticmethod
    def search_table_for_new_diners(i_restaurant_tables: list[Table], i_clients: list[Diner]):
        for table in i_restaurant_tables:
            if table.get_tables_diners() is None or len(table.get_tables_diners()) == 0:
                table.add_clients(i_clients)
                break
        else:
            pr_red("The Restaurant is FULL!!! Wait for an empty table ")

    # Waiter method that adds client to input table
    def add_clients_to_table(self, i_tables):
        number_of_clients = int(input("Enter the number of diners for the tables : "))
        print_cyan(number_of_clients)
        list_of_diners: list[Diner] = list()
        for index in range(number_of_clients):
            client_name = input("Enter the diner's name : ")
            print_cyan(client_name)
            list_of_diners.append(Diner(client_name))
        number_of_table = int(input("Enter the number of the table you want to add the diners to : "))
        for table in i_tables:
            if table.get_table_number() == number_of_table:
                table.add_clients(list_of_diners)
                break
        else:
            pr_red(f"Could not find table No.{number_of_table}")

    # Waiter method that removes client from a input table
    def remove_client_from_table(self: Waiter, restaurant_tables: list[Table]):
        number_of_clients = int(input("Enter the number of diners you want remove from the tables : "))
        print_cyan(number_of_clients)
        list_of_diners: list[Diner] = list()
        for index in range(number_of_clients):
            client_name = input("Enter the diner's name : ")
            print_cyan(client_name)
            list_of_diners.append(Diner(client_name))
        number_of_table = int(input("Enter the number of the table you want to remove client from : "))

        for table in restaurant_tables:
            if table.get_table_number() == number_of_table:
                table_diners: list[Diner] = table.get_tables_diners()
                for find_client in list_of_diners:
                    for table_client in table_diners:
                        if find_client.get_name() == table_client.get_name():
                            print_cyan(f"Client : {find_client.get_name()} removed from table")
                            table.remove_client(find_client)
                            list_of_diners.remove(find_client)
                for diner in list_of_diners:
                    pr_red(f"Could not find clients : {diner.get_name()} in table : {number_of_table}")
                break
        else:
            pr_red(f"Could not find table No.{number_of_table}")

    # Waiter Serving table method
    @staticmethod
    def serve_table(table: Table):
        for client in table.get_tables_diners():
            client.remove_orders_from_order_waiting_list(client.get_orders_waiting_list())
        print_cyan(f"Food has served for table number : {table.get_table_number()}")

    # Waiter Searching for diner method
    def search_for_diner(self, i_restaurant_tables: list[Table]):
        diner_name = input("Enter diners name for a search")
        self.search_for_client(i_restaurant_tables, diner_name)

    # Waiter cleaning the table
    def clean_table(self: Waiter):
        table_num = int(input("Enter a tables number"))
        for table in self.get_tables_i_waiter():
            if table.get_table_number() == table_num:
                print_cyan(f"Cleaning table No. : {table.get_table_number()}")
                for i in range(5):
                    time.sleep(1)
                    print_cyan_end(".")
                print()
                print_cyan("Table cleaned")
                break
        else:
            print_cyan("It is not one of my tables or you entered an invalid table number")

    # Waiter Gets client form tables
    @staticmethod
    def get_client_in_table(number_of_table: int, restaurant_tables: list[Table]) -> list[Diner]:
        for table in restaurant_tables:
            if table.get_table_number() == number_of_table:
                return table.get_tables_diners()
        else:
            pr_red(f"Could not find table No.{number_of_table}")

    # Waiter Search client form tables
    @staticmethod
    def search_for_client(i_restaurant_tables, diner_name: str) -> Diner:
        for table in i_restaurant_tables:
            for diner in table.get_tables_diners():
                if diner.get_name() == diner_name:
                    print_cyan(f"Diner : {diner.get_name()} has found in table : {table.get_table_number()} and returned ")
                    return diner
        else:
            pr_red(f"Could not find Diner {diner_name} in the restaurant")