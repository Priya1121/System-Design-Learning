
from .IDevice import IDevice

class Speaker(IDevice):
    def speakerApi(self):
        return print("Playing on speaker")