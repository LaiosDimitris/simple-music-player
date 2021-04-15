from . import FileManager
import vlc

vlc.MediaListPlayer

class VlcPlayer(vlc.Instance):
    """
    VlcPlayer class that uses vlc to play 
    individual tracks, playlists and youtube videos.
    
    """
    def __init__(self) -> None:
        super().__init__()
        self.__mediaPlayer = self.media_player_new()
        