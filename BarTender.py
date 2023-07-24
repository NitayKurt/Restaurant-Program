from datetime import datetime
from DAO.BarTenderOrder import BarTenderOrder
from Staff.Employee import Employee
from UI.ColorPrint import print_cyan, pr_red


class BarTender(Employee, BarTenderOrder):
    # Waiter Ctor, with Employee as a Parent and WaiterOrder as Interface
    def __init__(self, i_first_name: str, i_last_name: str, i_age: int, i_seniority: float, i_phone_number: str):
            Employee.__init__(self, i_first_name, i_last_name, i_age, i_seniority, i_phone_number)
            # Use when calling one parent Ctor
            # super().__init__(self, i_first_name, i_last_name, i_age, i_seniority, i_phone_number)

            # call when implementing more then one parent
            # Employee().__init__()
            # SecInheritingClass().__init_()

            self.__m_start_work_time = datetime.now()
            self.__m_end_work_time = datetime
            print_cyan(
                f"Bar tender: {self.get_first_name()} with the ID of :{self.get_employee_id()} has started working\n")

    # Print this bar tender
    def print_employee(self) -> None:
            print(f"""
             Bar tender's ID: {Employee.get_employee_id()}
             Bar tender's first name : {Employee.get_first_name(self)}
             Bar tender's last name : {Employee.get_last_name(self)}
             Bar tender's seniority: {Employee.get_seniority(self)}
             Bar tender's phone number: {Employee.get_phone_number(self)}
             Bar tender's start_work_time: {Employee.get_start_work_time(self)}
             Bar tender's end_work_time: {Employee.get_end_work_time(self)}
             """)

    # BarTender clean the bar on morning
    def clean_bar_on_morning(self) -> None:
        print_cyan(f"{Employee.get_first_name(self)} just cleaned the bar")