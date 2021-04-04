from pathvalidate import sanitize_filename, validate_filename
from youtubesearchpython import SearchVideos
import youtube_dl
import pafy
import json

class Youtube:
    """
    Youtube class for searching 
    videos from youtube.

    """
    def __init__(self) -> None:
        pass

    def search(self, query: str) -> dict:
        """
        Returns information in a dictionary of
        the first video it finds based on the query .

        """
        return self.__search(query)

    def download(self, url: str, title: str, destination='..\\..\\music\\tracks') -> bool:
        """
        Downloads the video's audio in mp3 format. 
        Returns True if the download was successful,
        otherwise it returns False.

        """
        return self.__download(url, title, destination)

    def __search(self, query: str):
        results = json.loads(SearchVideos(keyword=query, max_results=1).result())
        video = pafy.new(self.search_results["url"])
        return {
            "title": results['search_result'][0]['link'],
            "url": results['search_result'][0]['title'],
            "thumbnail": video.bigthumbhd,
            "length": int(video.length),
            "video": video.getbest().url,
        }

    def __generateValidFilename(self, title: str):
        try:
            validate_filename(self.search_results['title'])
            valid_title = self.search_results['title']
        except Exception as e:
            valid_title = sanitize_filename(self.search_results['title'])

    def __moveFileToTracksFolder(self, title: str, destination: str):
        """
        YoutubeDL downloads files in the current working directory,
        so we need to move the downloaded file to the destination
        of our choice.
        
        """
        filename = self.__generateValidFilename(title)

    def __download(self, url: str, title: str, destination: str):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }]}
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.__moveFileToTracksFolder(title, destination)
            return True
        except Exception as e:
            print(f'An error occured while downloading track from {url}\n{e}')
            return False