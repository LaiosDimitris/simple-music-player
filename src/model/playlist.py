from . import Track

class Playlist:
    """
    Playlist class that takes a list of Track objects
    
    """
    def __init__(self, tracks: list) -> None:
        self.__tracks = tracks

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