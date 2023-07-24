import time
from UI.ColorPrint import print_cyan_end, print_cyan
import winsound
from Staff import Employee


class BarTenderOrder():
    #clean the bar
    def clean_bar(self):
        # print_cyan(f"{Employee.get_first_name(self)} just cleaned the windows")
        for i in range(5):
            time.sleep(1)
            print_cyan_end(".")
        print()
        print_cyan("The bar is clean!")

    #make order of drinks
    def make_order_by_waiter(self):
        for i in range(5):
            time.sleep(1)
            print_cyan_end(".")
        print()
        print_cyan("The drinks are ready!")

    #ring the bell when the order is ready
    def ring_the_bell(self):
        time.sleep(0.5)
        for i in range(3):
            freq = 800
            dur = 400
            winsound.Beep(freq, dur)
        print("Golo golo!!! (S.G)")
