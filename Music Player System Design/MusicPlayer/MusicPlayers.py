import threading
from Song import Song
from Playlist import Playlist
from .NextModes.NextContext import NextContext
from Device.DeviceFactory import DeviceFactory
from .ButtonCommands.NextButton import NextButton
from .ButtonCommands.NextSongCmd import NextSongCmd

class MusicPlayers:
    
    _instance = None
    _lock = threading.Lock()
    

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, currentSong:Song, currentPlaylist:Playlist,currentIndex,currentMode:NextContext,device:DeviceFactory):
        self.currentSong = currentSong
        self.currentPlaylist = currentPlaylist
        self.currentIndex = currentIndex
        self.currentMode = currentMode 
        self.device = device
        
        # Initialize Command Pattern components internally
        self.next_cmd = NextSongCmd(self.currentMode)
        self.next_button = NextButton(self.next_cmd)


    def play(self):
        print(f"playing the song {self.currentSong.songName}")
    
    def pause(self):
        print(f"Paused the song {self.currentSong}")
    
    def next_track(self):
        """Uses Command Pattern internally to get next song"""
        next_song = self.next_button.playnext()  # Executes the command
        self.currentIndex += 1
        self.currentSong = next_song
        return next_song
        
    def previous(self, song:Song):
        pass    
