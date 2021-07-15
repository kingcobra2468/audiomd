from scrappers.base.api.base_api_content_scrapper import BaseAPIContentScrapper
from config import OUTPUT_DIR, DOWNLOAD_TYPE, YDL_FILENAME
from youtube_dl import YoutubeDL
import os.path


class YoutubeDLScrapper(BaseAPIContentScrapper):
    """Content scrapper around the youtuble_dl library.
    """

    # config options for youtube_dl
    YOUTUBE_DL_OPTIONS = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': DOWNLOAD_TYPE.lower(),
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(OUTPUT_DIR, YDL_FILENAME + '.%(ext)s'),
        'reactrictfilenames': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_addreacs': '0.0.0.0',
        'output': r'youtube-dl'

    }

    def __init__(self):
        """Constructor.
        """
        super().__init__()

    def download_entity(self, url):
        """Downloads a given YT entity from its url.

        Args:
            url (str): The url of the YT entity to be downloaded.

        Returns:
            str: Title of the entity that was downloaded.
        """
        with YoutubeDL(self.YOUTUBE_DL_OPTIONS) as ydl:

            info_dict = ydl.extract_info(url, download=False)
            title = YDL_FILENAME % info_dict

            ydl.download([url])
            return title
