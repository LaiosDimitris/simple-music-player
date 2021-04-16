from . import Track

class Playlist:
    """
    Playlist class that takes a list of Track objects
    
    """
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__tracks = []

    def addTrack(self, track: Track) -> None:
        """
        Adds a track to the playlist.
        
        """
        self.__addTrack(track)

    def removeTrack(self, track: Track) -> None:
        """
        Removes first occurence of provided track
        from the playlist.
        
        """
        self.__removeTrack(track)

    def getPlaylistName(self) -> str:
        """
        Returns the playlists name.
        
        """
        return self.__getPlaylistName()

    def getTrackFilenames(self) -> list:
        """
        Returns a list of filenames of the playlist's tracks.
        
        """
        return self.__getTrackFilenames()

    def getTrackTitles(self) -> list:
        """
        Returns a list of the titles of the playlist's tracks.
        
        """
        return self.__getTrackTitles()

    def getDuration(self) -> int:
        """
        Returns the playlist's total duraion in seconds.
        
        """
        return self.__getDuration()

    def getTrackCount(self) -> int:
        """
        Returns the amount of tracks in the playlist.

        """
        return self.__getTrackCount()

    def isEmpty(self) -> bool:
        """
        Returns True if the playlist is empty.
        Otherwise it returns False.

        """
        return self.__isEmpty()

    def __addTrack(self, track: Track):
        self.__tracks.append(track)

    def __removeTrack(self, track: Track):
        self.__tracks.remove(track)

    def __getPlaylistName(self):
        return self.__name

    def __getTrackFilenames(self):
        return [track.getFilename() for track in self.__tracks]

    def __getTrackTitles(self):
        return [track.getTitle() for track in self.__tracks]

    def __getDuration(self):
        return sum([track.getLength() for track in self.__tracks])

    def __getTrackCount(self):
        return len(self.__tracks)

    def __isEmpty(self):
        return len(self.__tracks) == 0