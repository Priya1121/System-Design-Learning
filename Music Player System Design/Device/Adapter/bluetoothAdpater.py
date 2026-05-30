
from ..IDevice import IDevice
from ..Bluetooth import Bluetooth
class bluetoothAdapter(IDevice):

        def __init__(self, bluetooth:Bluetooth):
                self.bluetooth = bluetooth

        def playOnDevice(self):
                return self.bluetooth.bluetoothApi()
        
