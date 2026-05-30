
from OrderCommand import OrderCommand
from Waiter import Waiter
from Chef import Chef
class main:

    if __name__ =="__main__":

        chef = Chef()
        kind = input()
        order = OrderCommand(chef,kind)
       
        waiter = Waiter(order)
       
        waiter.takeOrder()

        waiter.palceOrder()

        


