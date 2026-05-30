class Subject:

    def __init__(self):
         
        self.observers = []
        self.temp = None

    def addObserver(self,newObserver):
          self.observers.append(newObserver)
    
    def removeObserver(self,observer):
         self.observers.remove(observer)

    def notify(self):
         for i in self.observers:
              i.update(self.temp)

    def set_temp(self,temp):
         self.temp = temp
         print(f"Temp is changed to  {temp}")

         self.notify()

         