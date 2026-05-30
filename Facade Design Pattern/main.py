
from MessageService import MessageService
from TransactionService import PaymentService
from ResturantService import ResturantService
from DeliveryService import DeliveryService
from FacadeLayer import FacdeLayer
class main:

    if __name__ == "__main__":
        
        notification = MessageService()
        payments = PaymentService()
        orders = ResturantService()
        deliveries = DeliveryService()
        facade = FacdeLayer(orders,  payments,notification, deliveries)

        facade.execute()
