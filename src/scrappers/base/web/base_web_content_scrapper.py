from selenium import webdriver
from config import GECKODRIVER_PATH, EXTENSIONS_DIR, OUTPUT_DIR
from abc import ABC, abstractmethod
import os


class BaseWebContentScrapper(ABC):
    """Base class for developing Selenium based content scrappers.
    """
    # Selenium preferences config for Firefox geckodriver
    PROFILE = webdriver.FirefoxProfile()
    PROFILE.set_preference('dom.popup_maximum', 0)
    PROFILE.set_preference('privacy.popups.showBrowserMessage', False)
    PROFILE.set_preference('browser.preferences.instantApply', True)
    PROFILE.set_preference('browser.download.folderList', 0)
    PROFILE.set_preference('browser.download.manager.showWhenStarting', False)
    PROFILE.set_preference('browser.download.dir', OUTPUT_DIR)
    PROFILE.set_preference('browser.helperApps.alwaysAsk.force', False)
    PROFILE.set_preference(
        'browser.helperApps.neverAsk.saveToDisk', 'audio/mpeg, video/mp4')
    PROFILE.set_preference(
        'browser.helperApps.neverAsk.openFile', 'audio/mpeg, video/mp4')

    def __init__(self):
        """Constructor.
        """
        self._driver = webdriver.Firefox(executable_path=GECKODRIVER_PATH,
                                         firefox_profile=self.PROFILE)
        self.__setup_extensions()

    def __setup_extensions(self):
        """Setups extensions for geckodriver if they are present.
        """
        for extension in os.listdir(EXTENSIONS_DIR):
            self._driver.install_addon(os.path.abspath(
                os.path.join(EXTENSIONS_DIR, extension)))

    @abstractmethod
    def download_entity(self, url):
        """Downloads a given YT entity from its url.

        Args:
            url (str): The url of the YT entity to be downloaded.

        Returns:
            str: Title of the entity that was downloaded.
        """
        pass