from Device.IDevice import IDevice
class Subject:
    def __init__(self, text):
        self.text = None
        self.observer = []

    def addObserver(self,newObserver : IDevice):
        self.observer.append(newObserver)
    
    def removeObserver(self,dltObserver :IDevice):
        self.observer.remove(dltObserver)
    
    def notify(self):
        for i in self.observer:
            i.update(self.text)
    
    def set_text(self,text):
        self.text = text
        print(f"Text is changed to {text}")
        self.notify()



