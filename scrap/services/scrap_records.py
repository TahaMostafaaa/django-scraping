from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import StaleElementReferenceException
from datetime import datetime


import logging

ignored_exceptions = (StaleElementReferenceException)

logger = logging.getLogger(__name__)


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

    def get_records(self):
        logger.warning("== Start Scrapping Records ==")
        try:        
            self.driver.get(self.url)
        except Exception as ex:
            print(ex)
        rows = WebDriverWait(self.driver, 30, ignored_exceptions=ignored_exceptions).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR,".row-list")))
        rows = rows[1:]
        records = []
        for idx, row in enumerate(rows):
            record_row = self.get_record(row)
            records.append(record_row)
            logger.warning(f"Record Num. {idx+1} Done")

        logger.warning("== Returning Records to save ==")
        return records

    def get_record(self, row):
        records = row.find_elements(By.XPATH, "./*")
        date,title,country,sectors,signed_amount = records[0].text,records[1].text,records[2].text,records[3].text,records[4].text

        return {
            "date": datetime.strptime(date, "%d %B %Y").date(),
            "title": title,
            "country": country,
            "sectors": sectors,
            "signed_amount": signed_amount,
        }