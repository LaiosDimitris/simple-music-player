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

    def __loadPlaylists(self):
        filepaths = [f'{self.__playlistPath}\\{file}' for file in os.listdir(self.__playlistPath) if file.endswith('.json')]
        playlists = []
        for file in filepaths:
            with open(file, 'r', encoding='utf-8') as jsonFile:
                playlists.append(json.load(jsonFile))
        return playlists

    def __createPlaylist(self, name: str):
        for file in os.listdir(self.__playlistPath):
            if file.endswith('.json'):
                with open(f'{self.__playlistPath}\\{file}', 'r', encoding='utf-8') as jsonFile:
                    if json.load(jsonFile)['name'] == name:
                        return False
        with open(f"{self.__playlistPath}\\{name.replace(' ', '-').lower()}.json", 'w', encoding='utf-8') as jsonFile:
            json.dump({"name": name, "tracks": []}, jsonFile, indent=4)
            return True

    def __addTrackToPlaylist(self, filepath, name: str):
        playlist = None
        for file in os.listdir(self.__playlistPath):
            if file.endswith('.json'):
                with open(f'{self.__playlistPath}\\{file}', 'r', encoding='utf-8') as jsonFile:
                    playlist = json.load(jsonFile)
                    if playlist['name'] == name:
                        playlist['tracks'].append(filepath)
                        with open(f'{self.__playlistPath}\\{file}', 'w', encoding='utf-8') as jsonFile:
                            json.dump(playlist, jsonFile, indent=4)
                        return

    def __removeTrackFromPlaylist(self, filepath: str, name: str):
        playlist = None
        for file in os.listdir(self.__playlistPath):
            if file.endswith('.json'):
                with open(f'{self.__playlistPath}\\{file}', 'r', encoding='utf-8') as jsonFile:
                    playlist = json.load(jsonFile)
                    if playlist['name'] == name:
                        playlist['tracks'].pop(playlist['tracks'].index(filepath))
                        with open(f'{self.__playlistPath}\\{file}', 'w', encoding='utf-8') as jsonFile:
                            json.dump(playlist, jsonFile, indent=4)
                        return

FileManager().removeTrackFromPlaylist('..\\music\\tracks\\shogeki.mp3', 'Yes Honey')