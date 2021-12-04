from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as E, wait
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.common.by import By

class MainPage():
    title = "Wikipedia"
    english_partial_link_text = "English"
    wait_time_out = 5

    def __init__(self, driver):
        self.driver = driver
        self.waitVariable = W(self.driver, self.wait_time_out)

    def test_title(self):
        assert self.title in self.driver.title

    def click_english_link(self):
        self.waitVariable.until(E.element_to_be_clickable((By.PARTIAL_LINK_TEXT,self.english_partial_link_text))).click()
    