
from INext import INext
from Playlist import Playlist

class Repeat(INext):
    def mode(self, playlist: Playlist, currentIndex):
        return playlist.song[currentIndex]
    

