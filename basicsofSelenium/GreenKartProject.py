from selenium import webdriver
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class TestRun(unittest.TestCase):
    WEBSITE = "https://rahulshettyacademy.com/seleniumPractise/#/"

    def setUp(self):
        self.driver = webdriver.Chrome("C:/seleniumdriver/chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.WEBSITE)
        self.wait = WebDriverWait(self.driver, 3)

    def greenKart(self):
        self.driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
        count = len(self.driver.find_elements_by_xpath("//button[@type='button']"))
        assert count == 3 
        butons = self.driver.find_elements_by_xpath("//div[@class='product-action']/button") # We are assigning all of locators. and there are 3 same button elements. so it will create 3 elemnts as array

        for buton in butons:
            buton.click()
        
        self.driver.find_elements_by_xpath("img[alt='Cart']").click()
        self.driver.find_elements_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
        wait = WebDriverWait(self.driver, 5)
        assert self.wait.until(ec.presence_of_element_located(By.CLASS_NAME, "promoCode"))
        self.driver.find_element_by_class_name("promoCode").send_key("rahulshettyacademy")
        self.driver.find_element_by_css_selector("button[class='promoBtn']").click()



if __name__ == "__main__":
    unittest.main()


