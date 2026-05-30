from IObserver import IObserver

class TVObserver(IObserver):

    def update(self, temp):
        return print(f"the temp is {temp} on TV")
