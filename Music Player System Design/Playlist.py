
import Song
class Playlist:

    def __init__(self,name):
        self.name = name
        self.song = []

    def addSong(self,song1:Song):
        self.song.append(song1)