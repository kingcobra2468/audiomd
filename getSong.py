from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

noGUI = Options()
noGUI.add_argument('--headless')
options = webdriver.FirefoxProfile()
options.set_preference("dom.popup_maximum", 0)
options.set_preference("privacy.popups.showBrowserMessage", False)
options.set_preference("browser.preferences.instantApply",True)
options.set_preference("browser.download.folderList",0)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir","/home/erik/Desktop/")
options.set_preference("browser.helperApps.alwaysAsk.force",False)
options.set_preference("browser.helperApps.neverAsk.saveToDisk","audio/mpeg")
options.set_preference("browser.helperApps.neverAsk.openFile","audio/mpeg")

browser = webdriver.Firefox(firefox_profile=options, firefox_options=noGUI)
browser.get('https://ytmp3.cc/')

with open('/home/erik/Documents/Programming/Python/mp3Downloader/musicUrl.txt', "r") as url:
    for Url in url:
        browser.get('https://ytmp3.cc/')
        currentWindow = browser.window_handles[0]
        url = browser.find_element_by_id('input')
        url.send_keys(Url.strip())
        convert = browser.find_element_by_id('submit')
        convert.submit()
        while True:
            try:
                download = browser.find_element_by_id('download').click()
                #download.submit()
                break
            except:
                time.sleep(5)
        try:
            if len(browser.window_handles) == 1:
            else:
                browser.switch_to.window(browser.window_handles[-1])
                browser.close()
                browser.switch_to.window(currentWindow)
        except:
            pass
browser.close()