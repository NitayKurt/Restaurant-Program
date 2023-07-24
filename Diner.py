from DM.MenuItem import MenuItem

# Diner's class
class Diner:
    def __init__(self, i_diners_name: str):
        self.__m_diners_name: str = i_diners_name
        self.__m_orders: list[MenuItem] = list()

    # Gets Diners name
    def get_name(self) -> str:
        return self.__m_diners_name

    # Gets Diners waiting orders
    def get_orders_waiting_list(self) -> list[MenuItem]:
        return self.__m_orders

    # Adding orders to orders waiting list
    # for 1 parameter - adding one an MenuItem object
    # for more then 1 parameter - adding list of menu item
    def add_order_to_order_waiting_list(self, *args) -> None:
        # In case when the args that pass is a one order
        if len(args) == 1 and isinstance(args, MenuItem):
            self.__m_orders.append(args)
        # In case when the args that pass is a list of order
        elif isinstance(args, list):
            args: list[MenuItem]
            for menu_item in args:
                self.__m_orders.append(menu_item)

    # removing orders from waiting orders list
    def remove_orders_from_order_waiting_list(self, *args) -> None:
        if len(args) == 1 and isinstance(args, MenuItem):
            self.__m_orders.remove(args)
        elif isinstance(args, list):
            for menu_item in args:
                self.__m_orders.remove(menu_item)

    # Prints diners name
    def print(self) -> None:
        print(f"Diner : {self.get_name()}")





