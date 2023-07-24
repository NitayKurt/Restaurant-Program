from Client.Diner import Diner
from DAO.ManagerOrder import ManagerOrder
from RestaurantLogic import Table
from Staff.Employee import Employee
from Staff.Waiter import Waiter
from UI.ColorPrint import print_cyan
from RestaurantLogic import Restaurant


# Manager class
class Manager(Employee, ManagerOrder):
    # Manager Ctor, with Employee as a Parent and ManagerOrder as Interface
    def __init__(self, i_first_name: str, i_last_name: str, i_age: int, i_seniority: float, i_phone_number: str):
        Employee.__init__(self, i_first_name, i_last_name, i_age, i_seniority, i_phone_number)
        self.__m_manage_waiters: list[Waiter] = list()

        # !!!! IMPORTANT NOTE this line of code should be in the parent!!!!! and not each child separately #
        print_cyan(f"Manager : {self.get_first_name()} with the ID of :{self.get_employee_id()} has started working\n")

    # Set this Manager's Employees
    def set_employee_i_manage(self, list_of_waiters: list[Employee]) -> None:
        self.__m_manage_waiters = list_of_waiters

    # Gets this Manager's Employees
    def get_employees_i_manage(self) -> list[Employee]:
        return self.__m_manage_waiters

    # print this Manager
    def print_employee(self) -> None:
        print(f"""
        Manager ID: {Employee.get_employee_id()}
        Manager first name : {Employee.get_first_name(self)}
        Manager last name : {Employee.get_last_name(self)}
        Manager seniority: {Employee.get_seniority(self)}
        Manager phone number: {Employee.get_phone_number(self)}
        Manager start_work_time: {Employee.get_start_work_time(self)}
        Manager end_work_time: {Employee.get_end_work_time(self)}
        Manager current shift waiters managed: {self.get_employees_i_manage()}
        """)
