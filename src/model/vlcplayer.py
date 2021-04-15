from . import FileManager
from mutagen.mp3 import MP3
import vlc

vlc.MediaListPlayer

class VlcPlayer:
    """
    VlcPlayer class that uses vlc to 
    play individual tracks, playlists
    and youtube videos.
    
    """
    def __init__(self) -> None:
        self.__vlc = vlc.Instance()
        self.__mediaPlayer = self.__vlc.media_list_player_new()
        