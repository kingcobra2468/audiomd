from scrappers.base.base_factory import BaseFactory
from scrappers.content.web.ytmp3.ytmp3_content_scrapper import YTMP3ContentScrapper
from scrappers.content.api.youtube_dl_scrapper import YoutubeDLScrapper


class ContentFactory(BaseFactory):
    """Factory for generating content scrappers.
    """

    def __init__(self):
        """Constructor.
        """
        super().__init__()

        self._options['ytmp3'] = YTMP3ContentScrapper
        self._options['youtube_dl'] = YoutubeDLScrapper
