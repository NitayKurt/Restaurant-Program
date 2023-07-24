from __future__ import annotations
from typing import TYPE_CHECKING
from RestaurantLogic import Table
if TYPE_CHECKING:
    from Staff.Manager import Manager


# RestaurantUI ManagerUI
class ManagerUI:
    # RestaurantUI Ctor
    def __init__(self, manager: Manager, __i_restaurant_tables: list[Table], __i_money):
        print(f"""
hey Manager : {manager.get_first_name() + " " + manager.get_last_name()}
press the option you want to execute:
1.Add complaint about a Waiter 
2.Clean table
3.List of employee in this shift
4.Current sum of this shift
Q.For exit
        """)
        try:
            # Input to identify what functionality the user needed from the printed UI
            input_number = (input("press the number for you role"))
        except Exception as e:
            print(e.args)
        if input_number == "1":
            manager.file_a_complaint(manager)
        elif input_number == "2":
            manager.clean_table()
        elif input_number == "3":
            manager.list_of_employee_in_this_shift()
        elif input_number == "4":
            print("Current sum of this shift is : ", __i_money, " NIS")
        elif input_number == "Q":
            print("You are taken to the main menu")
        else:
            print("The number you have enter is not valid. You are taken to the main menu")