from scrappers.content.web.ytmp3.pages.ytmp3 import YTmp3
from scrappers.base.web.base_web_content_scrapper import BaseWebContentScrapper

class YTMP3ContentScrapper(BaseWebContentScrapper):
    """Manages Selenium(Firefox webdriver) session for YT download.
    """

    def __init__(self):
        """Constructor
        """
        super().__init__()
        self._ytmp3 = YTmp3(self._driver)

    def download_entity(self, url):
        """Downloads a YT entity

        Args:
            url (str): YT url to be downloaded

        Returns:
            str: Title of the video downloaded
        """
        self._ytmp3.enter_yt_link(url)
        self._ytmp3.download_yt_entity()

        title = self._ytmp3.get_title_downloaded_entity()

        self._ytmp3.close()

        return title
