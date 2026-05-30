
from MessageService import MessageService
from TransactionService import PaymentService
from ResturantService import ResturantService
from DeliveryService import DeliveryService

class FacdeLayer:

    notification = MessageService()
    payments = PaymentService()
    orders = ResturantService()
    deliveries = DeliveryService()

    def __init__(self, orders,  payments,notification, deliveries):
        self.notification = notification
        self.payments = payments
        self.orders = orders
        self.deliveries = deliveries

    def execute(self):
       
        self.orders.order()
        self.payments.payment()
        self.notification.notify()
        
        self.deliveries.delivered()

        


