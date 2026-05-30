from INext import INext
from Playlist import Playlist

class NormalMode(INext):

    def mode(self,playlist :Playlist, currentIndex):
        if currentIndex==len(playlist.song)-1:
            return playlist.song[0]
        return playlist.song[currentIndex+1]
            
