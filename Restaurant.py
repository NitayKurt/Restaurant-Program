from Client.Diner import Diner
from Staff.BarTender import BarTender
from Staff.Employee import Employee
from Staff.Manager import Manager
from Staff.Waiter import Waiter
from RestaurantLogic.Table import Table
from UI.ColorPrint import pr_red
from UI.ResturantUI import RestaurantUI



# Our Project class
class Restaurant:
    def __init__(self, *args: list):
        if len(args) == 0:
            # create list of managers waiters bartenders and restaurant tables
            self.__m_managers: list[Manager] = list()
            self.__m_waiters: list[Waiter] = list()
            self.__m_bar_tenders: list[BarTender] = list()
            self.__m_restaurant_tables: list[Table] = self.get_tables()
            self.__m_money = 0

    # Starting point the project/class
    def open_restaurant(self) -> None:
        self.__m_waiters = self.get_waiters()
        self.set_waiters_and_bind_tables(self.__m_waiters, self.__m_restaurant_tables)
        self.__m_bar_tenders = self.get_bar_tenders()
        __list_of_employee:list[Employee] = list()
        for waiter in self.__m_waiters:
            __list_of_employee.append(waiter)
        for barTender in self.__m_bar_tenders:
            __list_of_employee.append(barTender)
        self.__m_managers = self.get_managers(__list_of_employee)
        self.restaurant_morning_prep()
        RestaurantUI(self.__m_managers, self.__m_waiters, self.__m_bar_tenders, self.__m_restaurant_tables, self.__m_money).ShowUI()

    # Get restaurant method
    def get_restaurant_tables(self) -> list[Table]:
        return self.__m_restaurant_tables

    # Get bar tenders method
    @staticmethod
    def get_bar_tenders() -> list[BarTender]:
        current_shift_bar_tenders: list[BarTender] = list()
        current_shift_bar_tenders.append(BarTender("Orel moshe", "Magori", 26, 3.5, "0526666666"))
        current_shift_bar_tenders.append(BarTender("Idan", "Yaron", 24, 0.2, "0541234567"))
        return current_shift_bar_tenders

    # Generating managers method
    @staticmethod
    def get_tables() -> list[Table]:
        return_list_of_tables: list[Table] = list()
        for table_number in range(1, 11):
            return_list_of_tables.append(Table(table_number))
        return return_list_of_tables

    # Generating managers method
    @staticmethod
    def get_managers(__list_of_employee:list[Employee]) -> list[Manager]:

        current_shift_managers: list[Manager] = list()
        manager = Manager("Oliver", "Hart", 27, 1.5, "05155512231")
        manager.set_employee_i_manage(__list_of_employee)
        current_shift_managers.append(manager)
        return current_shift_managers

    # Generating managers method
    def set_managers(self, current_shift_managers: list[Manager]) -> None:
        self.__m_managers = current_shift_managers

    # Generating waiters method
    @staticmethod
    def get_waiters() -> list[Waiter]:
        pr_red(f"(!!!ID presented for functionality options only!!!)")
        current_shift_waiters: list[Waiter] = list()
        current_shift_waiters.append(Waiter("Liam", "Barlowe", 27, 0, "05155512231"))
        current_shift_waiters.append(Waiter("Noah", "Caddel", 27, 1.5, "05155512231"))
        current_shift_waiters.append(Waiter("Elijah", "Hart", 27, 1.5, "05155512231"))
        current_shift_waiters.append(Waiter("William", "Katz", 27, 1.5, "05155512231"))
        current_shift_waiters.append(Waiter("James", "Laurier", 27, 1.5, "05155512231"))
        current_shift_waiters.append(Waiter("Benjamin", "Madden", 27, 1.5, "05155512231"))
        current_shift_waiters.append(Waiter("Lucas", "Elrod", 27, 1.5, "05155512231"))
        current_shift_waiters.append(Waiter("Lucas", "Whitlock", 27, 1.5, "05155512231"))
        current_shift_waiters.append(Waiter("Henry", "Cromwell", 27, 1.5, "05155512231"))
        current_shift_waiters.append(Waiter("Alexander", "Monroe", 27, .5, "05155512231"))
        return current_shift_waiters

    # Binding waiters and tables method
    def set_waiters_and_bind_tables(self, current_shift_waiters: list[Waiter],
                                    i_restaurant_tables: list[Table]) -> None:
        self.__m_waiters = current_shift_waiters
        for i in range(len(i_restaurant_tables)):
            table_bind_waiter: list[Table] = list()
            table_bind_waiter.append(i_restaurant_tables[i])
            self.__m_waiters[i].set_tables_i_waiter(table_bind_waiter)

    # Restaurant morning prep method
    def restaurant_morning_prep(self) -> None:
        for waiter in self.__m_waiters:
            waiter.clean_windows()
        print()
        for barTender in self.__m_bar_tenders:
            barTender.clean_bar_on_morning()



