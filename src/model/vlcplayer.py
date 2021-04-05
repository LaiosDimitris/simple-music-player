from .filemanager import FileManager
from mutagen.mp3 import MP3
import vlc

vlc.MediaPlayer

class VlcPlayer:
    """
    VlcPlayer class that uses vlc to 
    play individual tracks, playlists
    and youtube videos.
    
    """
    def __init__(self) -> None:
        self.__vlc = vlc.Instance()
        self.__mediaPlayer = self.__vlc.media_player_new()
        self.__tracks = []
        self.__playlists = []
        self.__state = {
            'state'     :   'stop',
            'volume'    :   100,
            'muted'     :   False,
            'autoplay'  :   False,
            'loop'      :   False,
        }
        self.track = {
            'index'     :   0,
            'name'      :   0,
            'length'    :   0,
            'pos'       :   0,
            'ended'     :   False,
            'youtube'   :   False
        }
        self.playlist = {
            'index'     :   0,
            'name'      :   '',
            'tracks'    :   []
        }

    def play(self, filepath=None) -> None:
        """
        Plays the given track from the filepath.
        If a track is already playing it stops the previous
        one and plays the new one. If player is paused and no
        filepath is passed it just resumes the player.
        
        """
        self.__play(filepath)

    def pause(self) -> None:
        """
        Pauses the current track. No effect if
        nothing is playing.
        
        """
        self.__pause()

    def stop(self) -> None:
        """
        Stops the player. No effect if
        nothing is playing.
        
        """
        self.__stop()

    def __play(self, filepath: str):
        self.__state['state'] = 'play'
        if filepath != None:
            self.__getTrackInfo(filepath)
            self.__mediaPlayer.stop()
            self.__mediaPlayer.set_media(vlc.Media(filepath))
        self.__mediaPlayer.play()

    def __pause(self):
        self.__state['state'] = 'pause'
        self.__mediaPlayer.pause()

    def __stop(self):
        self.__state['state'] = 'stop'
        self.__mediaPlayer.stop()

    def __getTrackInfo(self, filepath: str):
        self.track['index'] = self.__tracks.index(filepath)
        self.track['name'] = filepath.replace('..\\music\\tracks\\', '')[:-4]
        self.track['length'] = int(MP3(filepath).info.length)
        self.track['pos'] = 0
        self.track['ended'] = False
        self.track['youtube'] = False