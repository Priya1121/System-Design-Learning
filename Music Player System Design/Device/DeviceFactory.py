from .IDevice import IDevice
from .Adapter.bluetoothAdpater import bluetoothAdapter
from .Adapter.speakerAdapter import speakerAdapter


class DeviceFactory:

    def getDevice(self,deviceType:str,device:IDevice):

        if deviceType  == 'Bluetooth':
            return bluetoothAdapter(device)
        elif deviceType == 'speaker':
            return speakerAdapter(device)
        