from Staff.BarTender import BarTender

class BarTenderUI:
    # WaiterUI Ctor
    def __init__(self, bar_tender: BarTender):

        print(f"""
hey bar_tender : {bar_tender.get_first_name() + " " + bar_tender.get_last_name()}
press the option you want to execute:
1.Clean bar
2.Make order by waiter
3.Ring the bell(Open the speaker)
           """)

        # Input to identify what functionality the user needed from the printed UI
        self.input_number: int
        try:
            self.input_number = input("press the number for you role")
        except Exception as e:
            print(e.args)

        if self.input_number == "1":
            bar_tender.clean_bar()

        elif self.input_number == "2":
            bar_tender.make_order_by_waiter()

        elif self.input_number == "3":
            bar_tender.ring_the_bell()
        else:
            print("You have entered a invalid number try again")
