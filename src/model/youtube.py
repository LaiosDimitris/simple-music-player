from pathvalidate import sanitize_filename, validate_filename
from youtubesearchpython import SearchVideos
import youtube_dl
import pafy
import json
import os

class Youtube:
    """
    Youtube class for searching videos 
    from youtube.

    """
    def __init__(self) -> None:
        pass

    def search(self, query: str) -> dict:
        """
        Returns information in a dictionary of
        the first video it finds based on the query .

        """
        return self.__search(query)

    def download(self, url: str, filename: str, destination='music\\tracks') -> bool:
        """
        Downloads the video's audio in mp3 format. 
        Returns True if the download was successful,
        otherwise it returns False.

        """
        return self.__download(url, self.search(url)['title'], destination)

    def __search(self, query: str):
        try:
            results = json.loads(SearchVideos(keyword=query, max_results=1).result())
            video = pafy.new(results['search_result'][0]['link'])
        except Exception as e:
            print(f'An error occured while searching Youtube for {query}\n{e}')
            return None
        return {
            "title": results['search_result'][0]['title'],
            "url": results['search_result'][0]['link'],
            "thumbnail": video.bigthumbhd,
            "length": int(video.length),
            "video": video.getbest().url,
        }

    def __generateValidFilename(self, filename: str):
        """
        The filenames YoutubeDL gives to the downloaded files
        is based on the video's title. If the video's title
        contains special characters then the file won't be
        created successfuly.

        """
        try:
            validate_filename(f'{filename}')
            return filename
        except Exception as e:
            return sanitize_filename(f'{filename}')

    def __moveFileToTracksFolder(self, filename: str, destination: str):
        """
        YoutubeDL downloads files in the current working directory,
        so we need to move the downloaded file to the destination
        of our choice.
        
        """
        fileToMove = [file for file in os.listdir() if file.endswith('.mp3')][0]
        validFilename = self.__generateValidFilename(filename)
        os.rename(fileToMove, f'{destination}\\{validFilename}.mp3')

    def __download(self, url: str, filename: str, destination: str):
        ydlOptions = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }]}
        try:
            with youtube_dl.YoutubeDL(ydlOptions) as ydl:
                ydl.download([url])
            self.__moveFileToTracksFolder(filename, destination)
            return True
        except Exception as e:
            print(f'An error occured while downloading track from {url}\n{e}')
            return False