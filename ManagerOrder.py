from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING

from Client.Diner import Diner
from DAO.WaiterOrder import WaiterOrder
from DM.MenuItem import MenuItem

from IDAO.ITableServing import ITableServing
from RestaurantLogic.Table import Table
from Staff.Waiter import Waiter
from Staff.BarTender import BarTender
from UI.ColorPrint import print_cyan, pr_red
from UI.ColorPrint import print_cyan_end
import time

from Enums.DessertPrices import DessertPrices
from Enums.DrinkPrices import DrinkPrices
from Enums.SideDishPrices import SideDishPrices
from Enums.StartPrices import StartPrices
from Enums.MainMealPrices import MainMealPrices
from RestaurantLogic import Restaurant

# Mechanism that make a module acknowledge the existence of circular import without the use of them
# Uses the 2 first lines
from UI.ResturantUI import RestaurantUI

if TYPE_CHECKING:
    from Staff.Manager import Manager

# Manager Interface implementation. implementing ITableServing Interface
class ManagerOrder():
    # Manager cleaning the table
    def clean_table(self):
        print("Calls the waiter to clear the table")


    def list_of_employee_in_this_shift(self:Manager):
        for employee in self.get_employees_i_manage():
            if issubclass(employee.__class__, Waiter):
                print(f"Waiter: {employee.get_first_name()}")
            if issubclass(employee.__class__, BarTender):
                print(f"BarTender: {employee.get_first_name()}")


    # Manager method that adds client to input table
    @staticmethod
    def file_a_complaint(manager: Manager):
        complaint = input("Enter a complaint")
        employee_id = int(input("Enter a employee's id"))
        for employee in manager.get_employees_i_manage():
            if employee.id == employee_id:
                if isinstance(employee, Waiter):
                    print(f"complaint filed on Waiter {employee.get_first_name()} {employee.get_last_name()} with"
                      , f"the complaint : {complaint}")
                    break
                elif isinstance(employee, BarTender):
                    print(f"complaint filed on BarTender {employee.get_first_name()} {employee.get_last_name()} with"
                          , f"the complaint : {complaint}")
                    break
        else:
            print("There is not employee with this id")

