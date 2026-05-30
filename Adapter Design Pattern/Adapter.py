from IDelivery import IDelivery

from Middleware import Middleware
class Adapter(IDelivery):

    def __init__(self, middleware:Middleware):
        self.middleware = middleware

    def deliver(self):
        return self.middleware.ship()
    
        
