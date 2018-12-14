from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import sys

class frameWork:

    noGUI = None
    options = None
    browser = None

    def preferences(self):
        self.noGUI = Options()
        self.noGUI.add_argument('--headless')
        self.options = webdriver.FirefoxProfile()
        self.options.set_preference(
            "dom.popup_maximum",
            0)
        self.options.set_preference(
            "privacy.popups.showBrowserMessage", 
            False)
        self.options.set_preference(
            "browser.preferences.instantApply",
            True)
        self.options.set_preference(
            "browser.download.folderList",
            0)
        self.options.set_preference(
            "browser.download.manager.showWhenStarting", 
            False)
        self.options.set_preference(
            "browser.download.dir","/home/erik/Desktop/")
        self.options.set_preference(
            "browser.helperApps.alwaysAsk.force",
            False)
        self.options.set_preference(
            "browser.helperApps.neverAsk.saveToDisk",
            "audio/mpeg, video/mp4")
        self.options.set_preference(
            "browser.helperApps.neverAsk.openFile",
            "audio/mpeg, video/mp4")

    def session(self, mode):
        self.preferences()
        if mode in "start":
            self.browser = webdriver.Firefox(firefox_profile=self.options, firefox_options=self.noGUI)
        else:
            time.sleep(10)
            self.browser.close()

    def download(self, type):
        with open('/home/erik/Documents/Programming/Python/mp3Downloader/musicUrl.txt', "r") as urls:
            for Url in urls:
                self.browser.get('https://ytmp3.cc/')
                currentWindow = self.browser.window_handles[0]
                url = self.browser.find_element_by_id('input')
                url.send_keys(Url.strip())
                
                if type == "mp4":
                    self.browser.find_element_by_id('mp4').click()

                convert = self.browser.find_element_by_id('submit')
                convert.submit()
                while True:
                    try:
                        self.browser.find_element_by_id('download').click()
                        break
                    except:
                        time.sleep(5)
                try:
                    if len(self.browser.window_handles) == 1:
                        pass
                    else:
                        self.browser.switch_to.window(self.browser.window_handles[-1])
                        self.browser.close()
                        self.browser.switch_to.window(currentWindow)
                except:
                    pass

if len(sys.argv) < 2:
    print('Input Error. Input mp3 or mp4 to convert to')
    exit()
else:
    session = frameWork()
    session.session('start')
    session.download(sys.argv[1])
    session.session('end')