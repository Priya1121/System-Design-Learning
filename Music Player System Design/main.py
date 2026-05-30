from Song import Song
from Playlist import Playlist
from MusicPlayer.MusicPlayers import MusicPlayers
from MusicPlayer.NextModes.ShuffleMode import ShuffleMode
from MusicPlayer.NextModes.NextContext import NextContext
from Device.Bluetooth import Bluetooth
from Device.DeviceFactory import DeviceFactory

if __name__ == '__main__':
    song1 = Song("As It Was", "Harry Style", "78")
    song2 = Song("Calm Down", "Salena Gomez", "90")
    song3 = Song("Die For You", "Lady Gaga", "67")
    song4 = Song("LMLY", "Jackson Wang", "56")

    playlist = Playlist("Favourite")
    playlist.addSong(song1)
    playlist.addSong(song4)
    playlist.addSong(song2)

    next_strategy = ShuffleMode()
    next_context = NextContext(next_strategy, playlist, 0)

    device_factory = DeviceFactory()
    device_type = Bluetooth()
    device_connected = device_factory.getDevice("Bluetooth", device_type)

    player =  MusicPlayers(song1, playlist, 0, next_context, device_connected)
    
    
    print("Player initialized successfully")

    player.play()
    device_connected.playOnDevice()
    
    # Use the player's built-in next_track method instead of exposing command pattern
    next_song = player.next_track()
    print(next_song.songName)


