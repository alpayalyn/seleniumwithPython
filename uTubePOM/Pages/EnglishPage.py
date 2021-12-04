from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as E, wait
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.common.by import By

class EnglishPage():
    SEARCH_ID_LOCATOR = "searchInput"
    TERM = "Software"
    WAIT_TIME_OUT = 5

    def __init__(self, driver):
        self.driver = driver
        self.waitVariable = W(self.driver, self.wait_time_out)
    
    def searchText(self):
        input_box_element = self.waitVariable.until(E.presence_of_element_located((By.ID, self.SEARCH_ID_LOCATOR)))
        input_box_element.send_keys(self.TERM)
        input_box_element.submit()
        self.waitVariable.until(E.title_contains(self.TERM))
