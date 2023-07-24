from Staff.Waiter import Waiter as Waiter
from RestaurantLogic import Table

global input_number


# WaiterUI Class
class WaiterUI:
    # WaiterUI Ctor
    def __init__(self, waiter: Waiter, i_restaurant_tables: list[Table]):

        print(f"""
hey waiter : {waiter.get_first_name() +" "+waiter.get_last_name()}
press the option you want to execute:
1.Search empty table for new customers
2.Clean table 
3.Take orders 
4.Cancel orders
5.Add clients to table
6.Remove client from table
7.Search diner in tables
8.Serve table
        """)

        # Input to identify what functionality the user needed from the printed UI
        self.input_number: int
        try:
            self.input_number = int(input("press the number for you role"))
        except Exception as e:
            print(e.args)

        if self.input_number == 1:
            try:
                waiter.new_restaurant_client(i_restaurant_tables)
            except Exception as e:
                print(e.args)

        elif self.input_number == 2:
            waiter.clean_table()

        elif self.input_number == 3:
            waiter.take_orders()

        elif self.input_number == 4:
            try:
                waiter.cancel_order()
            except Exception as e:
                print(e.args)

        elif self.input_number == 5:
            try:
                waiter.add_clients_to_table(i_restaurant_tables)
            except Exception as e:
                print(e.args)

        elif self.input_number == 6:
            try:
                waiter.remove_client_from_table(i_restaurant_tables)
            except Exception as e:
                print(e.args)

        elif self.input_number == 7:
            waiter.search_for_diner(i_restaurant_tables)

        elif self.input_number == 8:
            # self.input_number = int(input("press the number of table"))
            input_number_table = int(input("press the number of table"))
            for table in waiter.get_tables_i_waiter():
                if table.get_table_number() == input_number_table:
                    # print("The food is served")
                    waiter.serve_table(input_number)
            # print(waiter.get_tables_i_waiter())
            # a = waiter.get_tables_i_waiter()[input_number_table - 1]
            # waiter.serve_table()
        else:
            print("You have entered a invalid number try again")
