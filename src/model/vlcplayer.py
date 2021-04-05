from .filemanager import FileManager
from mutagen.mp3 import MP3
import vlc

class VlcPlayer:
    """
    VlcPlayer class that uses vlc to 
    play individual tracks, playlists
    and youtube videos.
    
    """
    def __init__(self) -> None:
        self.tracks = FileManager().loadTracks()
        self.playlists = FileManager().loadPlaylists()
        self.__vlc = vlc.Instance()
        self.__mediaPlayer = self.__vlc.media_player_new()
        self.__state = {
            'state'     :   'start',
            'volume'    :   100,
            'muted'     :   False,
            'autoplay'  :   False,
            'loop'      :   False,
        }
        self.trackState = {
            'index'     :   0,
            'name'      :   '',
            'from'      :   '',
            'length'    :   0,
            'pos'       :   0,
            'ended'     :   False,
            'youtube'   :   False,
        }
        self.playlistState = {
            'index'     :   0,
            'name'      :   'All Tracks',
            'tracks'    :   self.tracks,
        }

    def play(self, filepath=None) -> None:
        """
        Plays the given track from the filepath.
        If a track is already playing it stops the previous
        one and plays the new one. If player is paused and no
        filepath is passed it just resumes the player.
        
        """
        self.__play(filepath)

    def playNext(self) -> None:
        """
        Plays the next song in the current playlist. If the 
        currently playing song is the last in the playlist,
        then play the 1st song in the playlist.
        
        """
        self.__playNext()

    def playPrevious(self) -> None:
        """
        Plays the previous song in the current playlist. If the 
        currently playing song is the first in the playlist,
        then play the last song in the playlist.
        
        """
        self.__playPrevious()

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

    def skip(self, pos: int) -> None:
        """
        Skips to a specified part of
        the song.
        
        """
        self.__skip(pos)

    def setPlaylist(self, playlistName: str) -> None:
        """
        Sets a new playlist.
        
        """
        self.__setPlaylist(playlistName)

    def setVolume(self, vol: int) -> None:
        """
        Sets the player's volume.
        
        """
        self.__setVolume(vol)

    def update(self):
        """
        Reloads all the tracks and playlists again.

        """
        self.__update()

    def __play(self, filepath: str):
        self.__state['state'] = 'play'
        if filepath != None:
            self.__mediaPlayer.stop()
            self.__setNewMedia(filepath)
        self.__mediaPlayer.play()
        print(self.trackState)

    def __playNext(self):
        if self.__state['state'] == 'start':
            return
        if self.trackState['from'] != self.playlistState['name']:
            self.__play(self.playlistState['tracks'][0])
            return
        # If the currently playing song is the last in the playlist,
        # then play the 1st song in the playlist.
        trackIndex = self.trackState['index']
        if trackIndex == len(self.playlistState['tracks']) - 1:
            self.__play(self.playlistState['tracks'][0])
        else:
            self.__play(self.playlistState['tracks'][trackIndex+1])

    def __playPrevious(self):
        if self.__state['state'] == 'start':
            return
        if self.trackState['from'] != self.playlistState['name']:
            self.__play(self.playlistState['tracks'][0])
            return
        # If the currently playing song is the last in the playlist,
        # then play the 1st song in the playlist.
        trackIndex = self.trackState['index']
        if trackIndex == 0:
            self.__play(self.playlistState['tracks'][-1])
        else:
            self.__play(self.playlistState['tracks'][trackIndex-1])

    def __pause(self):
        self.__state['state'] = 'pause'
        self.__mediaPlayer.pause()

    def __stop(self):
        self.__state['state'] = 'stop'
        self.__mediaPlayer.stop()

    def __skip(self, pos: int):
        # Vlc set_position method takes as argument a float between
        # 0 and 1, 0 being the start of the track and 1 being the end.
        # We need to calculate the correct number to pass to set_position
        # based on the length of the track in seconds and the position
        # we want to skip to.
        posValue = ((pos * 100) / self.trackState['length']) / 100
        self.__mediaPlayer.set_position(posValue)

    def __setVolume(self, vol: int):
        if vol > 100:
            self.__mediaPlayer.audio_set_volume(100)
        elif vol < 0:
            self.__mediaPlayer.audio_set_volume(0)
        else:
            self.__mediaPlayer.audio_set_volume(vol)

    def __setPlaylist(self, name: str):
        for i, playlist in enumerate(self.playlists):
            if playlist['name'] == name:
                self.__setPlaylistInfo(playlist, i)
                return

    def __update(self):
        self.tracks = FileManager().loadTracks()
        self.playlists = FileManager().loadPlaylists()

    def __setTrackInfo(self, filepath: str):
        self.trackState['index'] = self.playlistState['tracks'].index(filepath)
        self.trackState['name'] = filepath.replace('..\\music\\tracks\\', '')[:-16]
        self.trackState['from'] = self.playlistState['name']
        self.trackState['length'] = int(MP3(filepath).info.length)
        self.trackState['pos'] = 0
        self.trackState['ended'] = False
        self.trackState['youtube'] = False

    def __setPlaylistInfo(self, playlist: dict, index: int):
        self.playlistState['index'] = index
        self.playlistState['name'] = playlist['name']
        self.playlistState['tracks'] = playlist['tracks']

    def __setNewMedia(self, filepath: str):
        self.__setTrackInfo(filepath)
        self.__mediaPlayer.set_media(vlc.Media(filepath))