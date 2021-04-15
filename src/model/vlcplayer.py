from . import FileManager
import vlc

vlc.MediaListPlayer

class VlcPlayer(vlc.Instance):
    """
    VlcPlayer class that uses vlc to play music.
    
    """
    def __init__(self) -> None:
        super().__init__()
        self.playlists = []
        self.__mediaPlayer = self.media_player_new()
    
