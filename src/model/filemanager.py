import json
import os

class FileManager:
    def __init__(self) -> None:
        pass

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

    def __loadTracks(self):
        return [f'..\\music\\tracks\\{file}' for file in os.listdir('..\\music\\tracks') if file.endswith('.mp3')]

    def __loadPlaylists(self):
        filepaths = [f'..\\music\\playlists\\{file}' for file in os.listdir('..\\music\\playlists') if file.endswith('.json')]
        playlists = []
        for file in filepaths:
            with open(file, 'r') as jsonFile:
                playlists.append(json.load(jsonFile))
        return playlists