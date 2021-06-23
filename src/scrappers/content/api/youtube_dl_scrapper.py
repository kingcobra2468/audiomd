from scrappers.base.api.base_api_content_scrapper import BaseAPiContentScrapper
from config import OUTPUT_DIR, DOWNLOAD_TYPE
from youtube_dl import YoutubeDL
import os.path

class YoutubeDLScrapper(BaseAPiContentScrapper):

    YOUTUBE_DL_OPTIONS = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': DOWNLOAD_TYPE.lower(),
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(OUTPUT_DIR, '%(title)s.%(ext)s'),
        'reactrictfilenames': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        # bind to ipv4 since ipv6 addreacses cause issues sometimes
        'source_addreacs': '0.0.0.0',
        'output': r'youtube-dl'

    }

    def __init__(self):
        super().__init__()

    def download_entity(self, url):
        """[summary]

        Args:
            url ([type]): [description]
        """
        with YoutubeDL(self.YOUTUBE_DL_OPTIONS) as ydl:
            
            info_dict = ydl.extract_info(url, download=False)
            title = info_dict['title']

            ydl.download([url])
            return title