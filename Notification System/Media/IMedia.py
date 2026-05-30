
from SimpleNotification import SimpleNotification

class IMedia(SimpleNotification):

    def __init__(self, baseText :SimpleNotification):
        self.baseText = baseText
    
    def addMedia(self):
        return self.baseText.notify()
    




        

