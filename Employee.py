from datetime import datetime
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, i_first_name: str,  i_last_name: str,
                 i_age: int, i_seniority: float, i_phone_number: str):
        if hasattr(Employee, "id"):
            Employee.id += 1
        else:
            Employee.id = 1
        self.id = Employee.id

        self.__m_start_work_time = datetime
        self.__m_end_work_time = datetime

        self.__m_first_name = i_first_name
        self.__m_last_name = i_last_name
        self.__m_age = i_age
        self.__m_seniority = i_seniority
        self.__m_phone_number = i_phone_number


    @staticmethod
    def get_employee_id() -> int:
        if Employee.id is not None:
            return Employee.id
        else:
            print("ID has not created yet")

    # @staticmethod
    def start_shift_this_time(self) -> None:
        self.__m_start_work_time = datetime.now().time()

    # @staticmethod
    def end_shift_this_time(self) -> None:
        self.__m_end_work_time = datetime.now().time()

    def get_start_work_time(self):
        return self.__m_start_work_time

    def set_start_work_time(self, i_set_start_work_time: datetime) -> None:
        self.__m_start_work_time = i_set_start_work_time

    def get_end_work_time(self):
        return self.__m_end_work_time

    def set_end_work_time(self, i_set_end_work_time: datetime) -> None:
        self.__m_end_work_time = i_set_end_work_time

    def get_first_name(self) -> str:
        return self.__m_first_name

    def get_last_name(self) -> str:
        return self.__m_last_name

    def get_age(self) -> int:
        return self.__m_age

    def get_seniority(self) -> float:
        return self.__m_seniority

    def get_phone_number(self) -> str:
        return self.__m_phone_number

    @abstractmethod
    def print_employee(self) -> None:
        pass
