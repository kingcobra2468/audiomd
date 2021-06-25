class BasePage:
    """Base page from which all Selenium-based scrappers could use
    as they traverse the web.
    """

    def __init__(self, driver):
        """Constructor.

        Args:
            driver (webdriver): Selenium webdriver object.
        """
        self._driver = driver

    def traverse_to_page(self, page_url):
        """Wrapper for traversing to a certain page.

        Args:
            page_url (str): Url for the page to be traversed.
        """
        self._driver.get(page_url)

    def close(self):
        """Terminates the webdriver and closes the driver.
        """
        self._driver.close()
