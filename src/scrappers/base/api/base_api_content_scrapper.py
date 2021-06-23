from abc import ABC, abstractmethod


class BaseAPIContentScrapper(ABC):
    """Base class for developing API/library driven content scrappers.
    """

    def __init__(self):
        """Constructor.
        """
        pass

    @abstractmethod
    def download_entity(self, url):
        """Downloads a given YT entity from its url.

        Args:
            url (str): The url of the YT entity to be downloaded.

        Returns:
            str: Title of the entity that was downloaded.
        """
        pass
