from RestaurantLogic.Table import Table
from Staff import Manager
from Staff.Waiter import Waiter
from UI.BarTenderUI import BarTenderUI
from UI.ManagerUI import ManagerUI
from UI.WaiterUI import WaiterUI as WaiterUI
from UI.ColorPrint import print_cyan, pr_red

from UI.ColorPrint import print_cyan_end
import time


# RestaurantUI Class
class RestaurantUI:
    # RestaurantUI Ctor
    def __init__(self, i_managers: list[Manager], i_waiters: list[Waiter], i__bar_tender: list[Waiter],
                 i_restaurant_tables: list[Table],  i_money: int):
        self.__m_managers: list[Manager] = i_managers
        self.__m_waiters: list[Waiter] = i_waiters
        self.__m_bar_tender: list[Waiter] = i__bar_tender
        self.__m_restaurant_tables: list[Table] = i_restaurant_tables
        self.__m_money = i_money

    # !!!IMPORTANT!!! Python3.9 ver does not support match case the is an match case example commented down below.
    # Match case supported in Python 3.10

    # Showing the UI method - show's the Restaurant functionality with ab Console UI
    # and therefore the root functionality will always return to this ShowUI which is the Restaurant UI
    def ShowUI(self) -> None:
        quit_app = True
        # A while condition that keep's UI running until user quites by entering an 'Q' input
        while quit_app:
            # Print UI input Functionality
            print("""
Hello and Welcome to Ariel's RestaurantUI . . . . . . . . . 
press the option you want to execute:
1.Diner Menu
2.Staff Menu
Q.To exit the application
                    """)

            # Input to identify what functionality the user needed from the printed UI
            input_number = input("Choose an option : ")
            if input_number == "1":
                self.Show_diner_UI()
            elif input_number == "2":
                self.Show_stuff_UI()
            elif input_number == "Q":
                quit_app = False
                print("Good Bye !!!")
            else:
                print("The number you have enter is not valid")

    # Showing the UI method - show's the Restaurant functionality with ab Console UI
    def Show_stuff_UI(self) -> None:
        print("""
press the option you want to execute:
1.Manager
2.Waiter
3.Bar tender
B.Back to the main menu
                            """)
        input_number = str()
        try:
            input_number = input("press the number for you role")
        except Exception as e:
            print(e.args)
        if input_number == "1":
            self.manager_check()
        elif input_number == "2":
            self.waiter_check()
        elif input_number == "3":
            self.bar_tender_check()
        elif input_number == "B":
            print("You are taken to the main menu")
        else:
            print("The number you have enter is not valid")

    # A method that check's if the manager exists and showing his UI
    def manager_check(self) -> None:
        try:
            employee_id = int(input("Enter manager id "))
            for manager in self.__m_managers:
                if manager.id == employee_id:
                    ManagerUI(manager, self.__m_restaurant_tables, self.__m_money)
                    break
            else:
                pr_red("Could not find manager")
        except Exception as e:
            pr_red(e.args)

    # A method that check's if the waiter exists and showing his UI
    def waiter_check(self) -> None:
        try:
            employee_id = int(input("Enter Waiter id "))
            for waiter in self.__m_waiters:
                if waiter.id == employee_id:
                    WaiterUI(waiter, self.__m_restaurant_tables)
                    break
            else:
                pr_red("Could not find Waiter")
        except Exception as e:
            pr_red(e.args)

    # A method that check's if the bar tender exists and showing his UI
    def bar_tender_check(self) -> None:
        try:
            employee_id = int(input("Enter Bar tender id "))
            for bar_tender in self.__m_bar_tender:
                if bar_tender.id == employee_id:
                    BarTenderUI(bar_tender)
                    break
            else:
                pr_red("Could not find bar tender")
        except Exception as e:
            pr_red(e.args)
        pass

    # Showing the UI method - show's the Restaurant functionality with ab Console UI
    def Show_diner_UI(self) -> None:
        print("""
press the option you want to execute:
1.Show Menu
2.Add to Order list
B.Back to the main menu
                                    """)
        input_number = input("press the number for you role")
        if input_number == "1":
            self.show_menu_UI()
        elif input_number == "2":
            self.add_to_order_list(self)
        elif input_number == "B":
            print("You are taken to the main menu")
        else:
            print("The number you have enter is not valid")
        pass
    def show_menu_UI(self) -> None:
        print_cyan("""
          ----------------Starters----------------
        
        -1- Scramble egg with bread..............40-NIS
        -2- Sandwich with Tuna...................20-NIS
        -3- Salad with vegetables................35-NIS
        -4- Hot bread with butter................20-NIS
        
          ---------------Main Meal----------------
        
        -5- Soup.................................40-NIS
        -6- Shakshuka............................45-NIS
        -7- Fish and Chips.......................60-NIS
        -8- Lazania..............................50-NIS
        
         ----------------Side Dish-----------------
        -9- Corn Pudding.........................35-NIS
        -10- Chips...............................30-NIS
        -11- Three Cheese Asparagus Gratin.......30-NIS
        
         -----------------Dessert------------------
        -12- Chocolate Chip Cookies..............30-NIS
        -13- Apple Pie...........................30-NIS
        -14 Cheese Cake..........................30-NIS
        
          -----------------Drinks-----------------
         
        -15- Water................................8-NIS
        -16- Coca-Cola...........................15-NIS
        -17- FuzeTea.............................10-NIS
        -18- Orange Juice........................12-NIS
        
        """)
        input_number1 = input("Choose B to go back : ")
        if input_number1 == "B":
            self.Show_diner_UI()
        else:
            print("The number you have enter is not valid. Return you to the main menu")

    @staticmethod
    def add_to_order_list(self) -> None:
        food_order_by_table_number = input("Insert your table number")
        print_cyan("""
                  ----------------Starters----------------

                -1- Scramble egg with bread..............40-NIS
                -2- Sandwich with Tuna...................20-NIS
                -3- Salad with vegetables................35-NIS
                -4- Hot bread with butter................20-NIS

                  ---------------Main Meal----------------

                -5- Soup.................................40-NIS
                -6- Shakshuka............................45-NIS
                -7- Fish and Chips.......................60-NIS
                -8- Lazania..............................50-NIS

                 ----------------Side Dish-----------------
                -9- Corn Pudding.........................35-NIS
                -10- Chips...............................30-NIS
                -11- Three Cheese Asparagus Gratin.......30-NIS

                 -----------------Dessert------------------
                -12- Chocolate Chip Cookies..............30-NIS
                -13- Apple Pie...........................30-NIS
                -14 Cheese Cake..........................30-NIS

                  -----------------Drinks-----------------

                -15- Water................................8-NIS
                -16- Coca-Cola...........................15-NIS
                -17- FuzeTea.............................10-NIS
                -18- Orange Juice........................12-NIS

                """)
        food_order_by_table_number: list = []
        sum = int(0);
        user_choose = input("Choose your food by dish number")
        while(user_choose != "B"):
            if(user_choose == "1"):
                sum += 40
                food_order_by_table_number.append("Scramble egg with bread")
            elif(user_choose == "2"):
                sum += 20
                food_order_by_table_number.append("Sandwich with Tuna")
            elif (user_choose == "3"):
                sum += 35
                food_order_by_table_number.append("Salad with vegetables")
            elif (user_choose == "4"):
                sum += 20
                food_order_by_table_number.append("Hot bread with butter")
            elif (user_choose == "5"):
                sum += 40
                food_order_by_table_number.append("Soup")
            elif (user_choose == "6"):
                sum += 45
                food_order_by_table_number.append("Shakshuka")
            elif (user_choose == "7"):
                sum += 60
                food_order_by_table_number.append("Fish and Chips")
            elif (user_choose == "8"):
                sum += 50
                food_order_by_table_number.append("Lazania")
            elif (user_choose == "9"):
                sum += 35
                food_order_by_table_number.append("Corn Pudding")
            elif (user_choose == "10"):
                sum += 30
                food_order_by_table_number.append("Chips")
            elif (user_choose == "11"):
                sum += 30
                food_order_by_table_number.append("Three Cheese Asparagus Gratin")
            elif (user_choose == "12"):
                sum += 30
                food_order_by_table_number.append("Chocolate Chip Cookies")
            elif (user_choose == "13"):
                sum += 30
                food_order_by_table_number.append("Apple Pie")
            elif (user_choose == "14"):
                sum += 30
                food_order_by_table_number.append("Cheese Cake")
            elif (user_choose == "15"):
                sum += 8
                food_order_by_table_number.append("Water")
            elif (user_choose == "16"):
                sum += 15
                food_order_by_table_number.append("Coca-Cola")
            elif (user_choose == "17"):
                sum += 10
                food_order_by_table_number.append("FuzeTea")
            elif (user_choose == "18"):
                sum += 12
                food_order_by_table_number.append("Orange Juice")
            elif (user_choose == "R"):#do not touch this!!!!
                #self.remove_from_order_list(food_order_by_table_number)
                print("What you want to remove: ", food_order_by_table_number)
                user_remove = input("Type the name of the food you want to remove from your order list: ")
                for food in food_order_by_table_number:
                    if (food == user_remove):
                        food_order_by_table_number.remove(food)
                        if(user_remove =="Scramble egg with bread"):
                            sum -= 40
                        elif(user_remove =="Sandwich with Tuna"):
                            sum -= 20
                        elif (user_remove == "Salad with vegetables"):
                            sum -= 35
                        elif (user_remove == "Hot bread with butter"):
                            sum -= 20
                        elif (user_remove == "Soup"):
                            sum -= 40
                        elif (user_remove == "Shakshuka"):
                            sum -= 45
                        elif (user_remove == "Fish and Chips"):
                            sum -= 60
                        elif (user_remove == "Lazania"):
                            sum -= 50
                        elif (user_remove == "Corn Pudding"):
                            sum -= 35
                        elif (user_remove == "Chips"):
                            sum -= 30
                        elif (user_remove == "Three Cheese Asparagus Gratin"):
                            sum -= 30
                        elif (user_remove == "Chocolate Chip Cookies"):
                            sum -= 30
                        elif (user_remove == "Apple Pie"):
                            sum -= 30
                        elif (user_remove == "Cheese Cake"):
                            sum -= 30
                        elif (user_remove == "Water"):
                            sum -= 8
                        elif (user_remove == "Coca-Cola"):
                            sum -= 15
                        elif (user_remove == "FuzeTea"):
                            sum -= 10
                        elif (user_remove == "Orange Juice"):
                            sum -= 12
                        print("This is the update list: ", food_order_by_table_number)
            else:
                    print("The number you have enter is not valid")
            user_choose = input("Choose your food OR Choose B to close your order OR Choose R to remove from order")

        print()
        print("This is what you ordered",food_order_by_table_number)
        print("The sum of your order is: ",sum ,"NIS")
        self.__m_money += sum
        print("Sending your order right now.....")
        for i in range(5):
            time.sleep(1)
            print_cyan_end(".")
        print()
        print_cyan("Your order is ready!")











# ===================== Match - case USE =========================
#     input_number = input("Choose an option : ")
#     match input_number:
#         case "1":
#             self.Show_diner_UI()
#         case "2":
#             self.Show_stuff_UI()
#         case "Q":
#             quit_app = False
#             print("Good Bye !!!")
#         case _:
#             print("The number you have enter is not valid")
#
#
# def Show_stuff_UI(self) -> None:
#     print("""
#     Hello and Welcome to Ariel's RestaurantUI . . . . . . . . .
#     press the option you want to execute:
#     1.Manager
#     2.Hostess
#     3.Waiter
#     4.Bar tender
#     Q.to exit the application
#                                 """)
#
#     input_number = str()
#     try:
#         input_number = input("press the number for you role")
#     except Exception as e:
#         print(e.args)
#     match input_number:
#         case "1":
#             try:
#                 employee_id: int = int(input("Enter manager id "))
#                 for manager in self.__m_managers:
#                     if manager.id == employee_id:
#                         # ADD YOUR IMPLEMENTATION HERE
#                         break
#                 else:
#                     print("Could not find manager")
#             except Exception as e:
#                 print(e.args)
#         case "2":
#             pass
#         # ADD YOUR IMPLEMENTATION HERE
#         case "3":
#             try:
#                 employee_id = int(input("Enter Waiter id "))
#                 for waiter in self.__m_waiters:
#                     if waiter.id == employee_id:
#                         WaiterUI(waiter, self.__m_restaurant_tables)
#                         break
#                 else:
#                     print("Could not find Waiter")
#             except Exception as e:
#                 # ADD YOUR IMPLEMENTATION HERE
#                 print(e.args)
#
#         case "4":
#             try:
#                 employee_id = int(input("Enter Bar tender id "))
#                 for bar_tender in self.__m_bar_tender:  # Class need to added
#                     if bar_tender.id == employee_id:
#                         # ADD YOUR IMPLEMENTATION HERE
#                         break
#                 else:
#                     print("Could not find manager")
#             except Exception as e:
#                 print(e.args)
#         case "Q":
#             print("Good Bye !!!")
#         case _:
#             print("The number you have enter is not valid")
