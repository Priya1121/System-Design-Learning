
from .IButton import IButton
from ..NextModes.NextContext import NextContext
class NextSongCmd(IButton):

    def __init__(self, next_context: NextContext):
        self.next = next_context
        # self.currentMode = currentMode

    def execute(self):
        return self.next.playNext()
    

        

        
