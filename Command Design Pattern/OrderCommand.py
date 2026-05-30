
from IOrder import IOrder
from Chef import Chef
class OrderCommand(IOrder):
    
        
    def __init__(self,chef :Chef, kind : str):
        self.chef = chef
        self.kind = kind

    def execute(self):
        return self.chef.cookPizza(self.kind)




