from typing import get_origin
from selenium import webdriver
import unittest
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class TestRun(unittest.TestCase):
    WEBSITE = "https://rahulshettyacademy.com/seleniumPractise/#/"
    SEARCH_BOX = (By.XPATH, "//input[@type='search']") # 
    ADD_TO_CART_COUNT = (By.CSS_SELECTOR, ".product-action") # THERE WILL BE 3 TITEMS WE WANT TO ADD
    ADD_TO_CART_STORE = (By.XPATH, "//div[@class='product-action']/button")
    GO_TO_CART = (By.XPATH, "//a[class='cart-icon']/img")
    PROCEED_TO_CHECKOUT = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    PROMO_CODE = (By.CSS_SELECTOR, "input.promocode")
    APPLY_CODE = (By.CSS_SELECTOR, "button[class='promoBtn']")

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.WEBSITE)
        self.wait = WebDriverWait(self.driver, 3)

    def testing_GreenKart(self):
        self.wait.until(ec.presence_of_all_elements_located(self.SEARCH_BOX)[0].send_keys("ber"))
        self.wait.until(ec.presence_of_all_elements_located(self.ADD_TO_CART_COUNT)).isDisplayed()
        count = len(self.wait.until(ec.presence_of_all_elements_located(self.ADD_TO_CART_STORE))) # Choose a tag which is common. For ex you have written ber and there will be items contains be rin their name. Those three items will have same parent tag. We use it then store them into an array.
        assert count == 3 
        butons = self.wait.until(ec.presence_of_all_elements_located(self.ADD_TO_CART_STORE)) # We are assigning all of locators. and there are 3 same button elements. so it will create 3 elemnts as array

        for buton in butons:
            print(buton)
            buton.click()

        self.wait.until(ec.presence_of_all_elements_located(self.GO_TO_CART))
        self.wait.until(ec.presence_of_all_elements_located(self.PROCEED_TO_CHECKOUT)) # Defined by the text it contained so its important from that perspective
        wait = WebDriverWait(self.driver, 5)        
        assert self.wait.until(ec.presence_of_element_located(self.PROMO_CODE))
        self.wait.until(ec.presence_of_all_elements_located(self.PROMO_CODE)).send_key("rahulshettyacademy")
        self.wait.until(ec.presence_of_all_elements_located(self.APPLY_CODE)).click()

testing = TestRun()

testing.setUp()
testing.testing_GreenKart()

if __name__ == "__main__":
    unittest.main()


