import json
import os

class FileManager:
    def __init__(self) -> None:
        self.__trackPath = '..\\music\\tracks'
        self.__playlistPath = '..\\music\\playlists'

    def loadTracks(self) -> list:
        """
        Returns all the filepaths of the tracks 
        from the tracks folder.
        
        """
        return self.__loadTracks()

    def loadPlaylists(self) -> list:
        """
        Returns all the json files in the
        playlists folder.
        
        """
        return self.__loadPlaylists()

    def createPlaylist(self, name: str) -> bool:
        """
        Creates a new playlist. If the playlist is 
        created successfuly it returns True. If a 
        playlist with the same name exists, it returns False. 
        
        """
        return self.__createPlaylist(name)

    def addTrackToPlaylist(self, filepath: str, name='All Tracks'):
        """
        Adds a track to the given playlist.
        
        """
        self.__addTrackToPlaylist(filepath, name)

    def removeTrackFromPlaylist(self, filepath: str, name='All Tracks'):
        """
        Removes a track from the given playlist.
        
        """
        self.__removeTrackFromPlaylist(filepath, name)
        
    def __loadTracks(self):
        return [f'{self.__trackPath}\\{file}' for file in os.listdir(self.__trackPath) if file.endswith('.mp3')]

    