from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class GreenKart:
    WEBSITE = "https://rahulshettyacademy.com/seleniumPractise/#/"

    def __init__(self):
        self.driver = webdriver.Chrome("C:/seleniumdriver/chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.WEBSITE)
        self.wait = WebDriverWait(self.driver, 15)

    def test(self):
        self.driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
        count = len(self.driver.find_elements_by_xpath("//button[@type='button']"))
        assert count == 3 
        butons = self.driver.find_elements_by_xpath("//div[@class='product-action']/button") #

        for buton in butons:
            buton.click()
        
        self.driver.find_elements_by_xpath("img[alt='Cart']").click()
        self.driver.find_elements_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
