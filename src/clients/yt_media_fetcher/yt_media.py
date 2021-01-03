from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from config import GECKODRIVER_PATH, EXTENSIONS_DIR
from clients.yt_media_fetcher.pages.ytmp3 import YTmp3
import os


class YTMedia:
    """Manages Selenium(Firefox webdriver) session for YT download.
    """
    # Selenium OPTIONS config
    OPTIONS = Options()
    OPTIONS.add_argument('--headless')

    # Selenium preferences config for Firefox geckodriver
    PROFILE = webdriver.FirefoxProfile()
    PROFILE.set_preference('dom.popup_maximum', 0)
    PROFILE.set_preference('privacy.popups.showBrowserMessage', False)
    PROFILE.set_preference('browser.preferences.instantApply', True)
    PROFILE.set_preference('browser.download.folderList', 0)
    PROFILE.set_preference('browser.download.manager.showWhenStarting', False)
    PROFILE.set_preference('browser.download.dir', '/home/erik/Desktop/')
    PROFILE.set_preference('browser.helperApps.alwaysAsk.force', False)
    PROFILE.set_preference(
        'browser.helperApps.neverAsk.saveToDisk', 'audio/mpeg, video/mp4')
    PROFILE.set_preference(
        'browser.helperApps.neverAsk.openFile', 'audio/mpeg, video/mp4')

    def __init__(self):
        """Constructor
        """
        self._driver = webdriver.Firefox(executable_path=GECKODRIVER_PATH,
                                         firefox_profile=self.PROFILE) # firefox_options=self.OPTIONS
        self.__setup_extensions()

        self._ytmp3 = YTmp3(self._driver)

    def __setup_extensions(self):
        """Setups extensions for geckodriver if present
        """
        for extension in os.listdir(EXTENSIONS_DIR):
            self._driver.install_addon(os.path.abspath(
                os.path.join(EXTENSIONS_DIR, extension)))

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
