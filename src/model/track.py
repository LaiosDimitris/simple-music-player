from mutagen.mp3 import MP3

class Track:
    """
    Track class which contains information
    of an mp3 file.
    
    """
    def __init__(self, filename: str) -> None:
        self.__filename = filename
    
    def getLength(self) -> int:
        """
        Get the track's length.
        
        """
        return self.__getLength()

    def getFilename(self) -> str:
        """
        Get the track's full filename.
        
        """
        return self.__getFilename()

    def getTitle(self) -> str:
        """
        Get the track's title.
        
        """
        return self.__getTitle()

    def rename(self, newTitle: str) -> None:
        """
        Rename the track.
        
        """
        self.__rename(newTitle)

    def __getLength(self):
        return int(MP3(self.__filename).info.length)

    def __getFilename(self):
        return self.__filename

    def __getTitle(self):
        return self.__filename.replace('music\\', '')[:-4]

    def __rename(self, newTitle: str):
        self.__filename.replace(self.__getTitle(), newTitle)