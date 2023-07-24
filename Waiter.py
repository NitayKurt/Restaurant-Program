from datetime import datetime

from DAO.WaiterOrder import WaiterOrder
from RestaurantLogic.Table import Table
from Staff.Employee import Employee
from UI.ColorPrint import print_cyan, pr_red


# Waiter class
class Waiter(Employee, WaiterOrder):
    # Waiter Ctor, with Employee as a Parent and WaiterOrder as Interface
    def __init__(self, i_first_name: str, i_last_name: str, i_age: int, i_seniority: float, i_phone_number: str):
        Employee.__init__(self, i_first_name, i_last_name, i_age, i_seniority, i_phone_number)

        self.__m_start_work_time = datetime.now()
        self.__m_end_work_time = datetime
        self.__m_serving_tables = None
        print_cyan(f"Waiter: {self.get_first_name()} with the ID of :{self.get_employee_id()} has started working\n")

    # Set this waiter tables
    def set_tables_i_waiter(self, list_of_tables: list[Table]) -> None:
        self.__m_serving_tables = list_of_tables

    # Get this waiter tables
    def get_tables_i_waiter(self) -> list[Table]:
        return self.__m_serving_tables

    # Print this waiter
    def print_employee(self) -> None:
        print(f"""
         Waiter ID: {Employee.get_employee_id()}
         Waiter first name : {Employee.get_first_name(self)}
         Waiter last name : {Employee.get_last_name(self)}
         Waiter seniority: {Employee.get_seniority(self)}
         Waiter phone number: {Employee.get_phone_number(self)}
         Waiter start_work_time: {Employee.get_start_work_time(self)}
         Waiter end_work_time: {Employee.get_end_work_time(self)}
         """)

    # Waiter's clean window method
    def clean_windows(self) -> None:
        print_cyan(f"{Employee.get_first_name(self)} just cleaned the windows")
