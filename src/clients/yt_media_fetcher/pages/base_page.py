class BasePage:

    def __init__(self, driver):

        self._driver = driver

    def traverse_to_page(self, page_url):

        self._driver.get(page_url)
    
    def close(self):
        self._driver.close()