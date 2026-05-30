
from .NextSongCmd import NextSongCmd
class NextButton:

    def __init__(self, nextSong:NextSongCmd):
        self.nextSong = nextSong 
        
    def playnext(self):
        return self.nextSong.execute()



        