
from IDevice import IDevice
class LaptopDevice(IDevice):
    def update(self,text):
        return print(f"Nofication in TV {text}")