from Playlist import Playlist
from .INext import INext
class NextContext:
    def __init__(self, next :INext,playlist:Playlist, currentIndex):
        self.next = next
        self.playlist = playlist
        self.currentIndex = currentIndex

    def playNext(self):
        return self.next.mode(self.playlist,self.currentIndex)
    