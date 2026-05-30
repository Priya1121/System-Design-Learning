from .INext import INext
import random
from Playlist import Playlist

class ShuffleMode(INext):

    def mode(self, playlist:Playlist, currentIndex):
        random_num = random.randrange(len(playlist.song))
        return playlist.song[random_num]
        
