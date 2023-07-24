from __future__ import annotations
from typing import TYPE_CHECKING

import Client.Diner as Diner
from UI.ColorPrint import print_cyan

# Mechanism that make a module acknowledge the existence of circular import without the use of them
# Uses the 2 first lines
if TYPE_CHECKING:
    from Staff.Waiter import Waiter


# Table class
class Table:
    def __init__(self, *args):
        # Ctor for creating a table with table number, list of waiters, list of diner
        if len(args) == 3:
            # = args[0]
            self.__m_tables_number: int
            self.__m_waiters: list[Waiter] = args[1]
            # = args[2]
            self.__m_diners: list[Diner]
        # Ctor for creating a table with only table number
        elif len(args) == 1:
            self.__m_tables_number: int = args[0]
            self.__m_diners: list[Diner] = list()
            self.__m_waiters: list[Waiter] = list()
        else:
            raise Exception("Ctor only takes 1 or 3 arguments")

    # Get the tables number
    def get_table_number(self) -> int:
        return self.__m_tables_number

    # preparing the table - cleaning arranging plates
    def prep_table(self) -> None:
        self.setting_table()

    # Setting the table method
    def setting_table(self) -> None:
        self.cleaning_the_tables()
        self.plates_arranging()

    # Cleaning the table method
    @staticmethod
    def cleaning_the_tables() -> None:
        print_cyan("the table is clean")

    # Arranging the table plates method
    @staticmethod
    def plates_arranging() -> None:
        print_cyan("Arranging plates")

    # Set's table waiters
    def set_waiters(self, i_waiters: list[Waiter]) -> None:
        self.__m_waiters = i_waiters

    # Adding table waiters
    def add_waiters(self, i_waiters: list[Waiter]) -> None:
        for waiter in i_waiters:
            self.__m_waiters.append(waiter)

    # Set's table clients
    def set_clients(self, i_clients: list[Diner]) -> None:
        if self.__m_diners is not None:
            self.__m_diners = i_clients

    # Adding table clients
    def add_clients(self, i_clients: list[Diner]) -> None:
        for client in i_clients:
            if client not in self.__m_diners:
                self.__m_diners.append(client)
                print_cyan(f"Client: {client.get_name()} is now sitting in table No. : {self.get_table_number()}")

    # Removing table clients
    def remove_client(self, i_client: Diner) -> None:
        for client in self.__m_diners:
            if client.get_name() == i_client.get_name():
                self.__m_diners.remove(client)

    # Getting the table clients\diners
    def get_tables_diners(self) -> list[Diner]:
        return_diners: list[Diner] = self.__m_diners
        return return_diners

    # Getting the table clients\diners
    def get_tables_waiters(self) -> list[Waiter]:
        return self.__m_waiters
