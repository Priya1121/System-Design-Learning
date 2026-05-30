from INotification import INotification

class SimpleNotification(INotification):
    text = "This is alert message"

    def __init__(self, text):
        self.text = text

    def notify(self):
        return self.text
