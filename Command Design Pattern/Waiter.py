
from OrderCommand import OrderCommand
class Waiter:

    def __init__(self, order:OrderCommand):
        self.order = order
       
       
    
    def takeOrder(self):
      
        
        print(f"1 order for {self.order.kind} pizza")


    def palceOrder(self):
        return self.order.execute()