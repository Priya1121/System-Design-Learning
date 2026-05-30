
from Device.IDevice import IDevice
class MobileDevice(IDevice):
    def update(self,text):
        return print(f"You got notification in mobile {text} ")