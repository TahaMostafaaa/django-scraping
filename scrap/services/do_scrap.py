from selenium import webdriver


class ScrapRecords:
    url = "https://www.eib.org/en/projects/loans/index.htm"
    page_count = 25


    def __init__(self):
        self.driver = webdriver.Remote(
            "http://selenium:4444/wd/hub", DesiredCapabilities.FIREFOX
        )

    def __del__(self):
        self.driver.quit()
        self.driver.close()

    