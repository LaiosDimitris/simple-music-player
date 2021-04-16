from . import Playlist
from . import Track
import json
import os

class FileManager:
    """
    FileManager class for managing I/O of files.
    
    """
    def __init__(self) -> None:
        self.__music = '..\\music'
        self.__tracks = '..\\music\\meta\\tracks.json'
        self.__playlists = '..\\music\\meta\\playlists.json'

    def addTrack(self, filename: str) -> None:
        """
        Adds a track in the music folder.
        
        """
        self.__addTrack(filename)

    def deleteTrack(self, filename: str) -> None:
        """
        Removes a track from the music folder.
        
        """
        self.__removeTrack(filename)

    def addTrackToPlaylist(self, filename: str, playlist: str) -> None:
        """
        Adds a track to a playlist.
        
        """
        self.__addTrackToPlaylist(filename, playlist)

    def removeTrackFromPlaylist(self, filename: str, playlist: str) -> None:
        """
        Removes a track from a playlist.
        
        """
        self.__removeTrackFromPlaylist(filename, playlist)
    
    def createPlaylist(self, playlist: str) -> None:
        """
        Creates a new playlist.
        
        """
        self.__createPlaylist(playlist)

    def deletePlaylist(self, playlist: str) -> None:
        """
        Deletes a playlist.
        
        """
        self.__deletePlaylist(playlist)