from scrappers.base.web.pages.base_page import BasePage
from config import DOWNLOAD_TYPE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class YTmp3(BasePage):
    """Selenium wrapper around ytmp3.cc site.
    """

    PAGE_URL = 'https://ytmp3.cc/'
    MODE_IDS = {
        'MP3': 'mp3',
        'MP4': 'mp4'
    }
    CONVERT_BTN = 'submit'
    URL_INPUT = 'input'
    YT_ENTITY_ID = "title"

    def __init__(self, driver):
        """Constructor.

        Args:
            driver (webdriver): Selenium webdriver object.

        Raises:
            ValueError: Raised if download type is not MP3/MP4.
        """
        super().__init__(driver)

        if DOWNLOAD_TYPE not in self.MODE_IDS.keys():
            raise ValueError('Config value for DOWNLOAD_TYPE is not valid')

        self.traverse_to_page(self.PAGE_URL)

    def download_yt_entity(self):
        """Performs a download of YT entity.
        """
        try:
            wait = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.ID, 'buttons')))
        except TimeoutException:
            print(f'Unable to download song.')
            self.close()

        self._driver.find_element_by_id(
            'buttons').find_elements_by_tag_name('a')[0].click()

    def get_title_downloaded_entity(self):
        """Gets the title of YT video that was download.

        Returns:
            str: Title of the video downloaded.
        """
        entity = self._driver.find_element_by_id('title')
        return entity.text

    def enter_yt_link(self, url):
        """Url of the YT entity to be downloaded.

        Args:
            url (str): YT url to be downloaded.
        """
        yt_entry = self._driver.find_element_by_id('input')
        yt_entry.send_keys(url.strip())

        convert = self._driver.find_element_by_id('submit')
        convert.submit()

    def select_download_type(self):
        """Specifies the download type for the converter.
        """
        self._driver.find_element_by_id(self.MODE_IDS[DOWNLOAD_TYPE]).click()
