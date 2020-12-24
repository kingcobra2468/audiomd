from clients.yt_media_fetcher.pages.base_page import BasePage
from config import DOWNLOAD_TYPE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class YTmp3(BasePage):

    PAGE_URL = 'https://ytmp3.cc/'
    MODE_IDS = {
        'MP3': 'mp3',
        'MP4': 'mp4'
    }
    CONVERT_BTN = 'submit'
    URL_INPUT = 'input'
    YT_ENTITY_ID = "title"

    def __init__(self, driver):

        super().__init__(driver)

        if DOWNLOAD_TYPE not in self.MODE_IDS.keys():
            raise ValueError('Config value for DOWNLOAD_TYPE is not valid')
        
        self.traverse_to_page(self.PAGE_URL)

    def download_yt_entity(self):
        
        wait = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.ID, "buttons")))

        self._driver.find_element_by_id(
            'buttons').find_elements_by_tag_name('a')[0].click()
    
    def get_title_downloaded_entity(self):

        entity = self._driver.find_element_by_id('title')
        return entity.text

    def enter_yt_link(self, url):

        yt_entry = self._driver.find_element_by_id('input')
        yt_entry.send_keys(url.strip())

        convert = self._driver.find_element_by_id('submit')
        convert.submit()

    def select_download_type(self):

        self._driver.find_element_by_id(self.MODE_IDS[DOWNLOAD_TYPE]).click()
