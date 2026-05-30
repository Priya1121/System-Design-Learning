from IObserver import IObserver

class MobileObserver(IObserver):

    def update(self,temp):
        print(f"the temp is {temp} on mobile")


