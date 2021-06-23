from scrappers.content.web.ytmp3.pages.ytmp3 import YTmp3
from scrappers.base.web.base_web_content_scrapper import BaseWebContentScrapper

class YTMP3ContentScrapper(BaseWebContentScrapper):
    """Content scrapper around the ytmp3.cc website.
    """

    def __init__(self):
        """Constructor.
        """
        super().__init__()
        self._ytmp3 = YTmp3(self._driver)

    def download_entity(self, url):
        """Downloads a given YT entity from its url.

        Args:
            url (str): The url of the YT entity to be downloaded.

        Returns:
            str: Title of the entity that was downloaded.
        """
        self._ytmp3.enter_yt_link(url)
        self._ytmp3.download_yt_entity()

        title = self._ytmp3.get_title_downloaded_entity()

        self._ytmp3.close()

        return title
