
from ..IDevice import IDevice
from ..Speaker import Speaker
class speakerAdapter(IDevice):
    def __init__(self, speaker:Speaker):
        self.speaker = speaker

    def playOnDevice(self):
        return self.speaker.speakerApi()
    
        
