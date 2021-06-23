from abc import ABC, abstractmethod
import os


class BaseAPiContentScrapper(ABC):
    """Base class for developing Selenium based content scrappers.
    """

    def __init__(self):
        """Constructor
        """
        pass
    
    @abstractmethod
    def download_entity(self, url):
        """Downloads a YT entity

        Args:
            url (str): YT url to be downloaded

        Returns:
            str: Title of the video downloaded
        """
        pass