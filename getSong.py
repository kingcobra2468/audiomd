from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import sys
import threading

class getContent(threading.Thread):

    noGUI = None
    options = None
    browser = None

    def __init__(self, link, type):
        threading.Thread.__init__(self)
        self.link = link;
        self.type = type
        self.preferences()
        self.browser = webdriver.Firefox(firefox_profile=self.options, firefox_options=self.noGUI)
    
    def __del__(self):
        self.browser.close()
        threading.Thread.join(self)
    
    @staticmethod
    def getUrl(path):
        while True:
            data = path.readline()
            if not data:
                break
            yield data

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
    
    def download(self):
        self.browser.get('https://ytmp3.cc/')
        currentWindow = self.browser.window_handles[0]
        url = self.browser.find_element_by_id('input')
        url.send_keys(self.link.strip())
        if self.type == "mp4":
            self.browser.find_element_by_id('mp4').click()
        convert = self.browser.find_element_by_id('submit')
        convert.submit()
        while True:
            try:
                self.browser.find_element_by_id('download').click()
                break
            except:
                time.sleep(5)
        try: #closes annoying pop-up windows
            if len(self.browser.window_handles) == 1:
                pass
            else:
                self.browser.switch_to.window(self.browser.window_handles[-1])
                self.browser.close()
                self.browser.switch_to.window(currentWindow)
        except:
            pass
    def run(self):
        self.download()

if len(sys.argv) < 2:
    print('Input Error. Input mp3 or mp4 to convert to')
    exit()
else:
    filePath = '/home/erik/Documents/Programming/Python/mp3Downloader/musicUrl.txt'
    urlFile = open(filePath, 'r')
    for url in getContent.getUrl(urlFile):
        getContent(url, sys.argv[1]).start()
    open(filePath, 'w').close() #empties file
