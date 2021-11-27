from selenium import webdriver
import unittest
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class TestRun(unittest.TestCase):
    WEBSITE = "https://www.lcwaikiki.com/tr-TR/TR"
    CATEGORY_PAGE_1 = (By.CSS_SELECTOR, '.sf-with-ul')
    PRODUCT_PAGE = (By.CSS_SELECTOR, '.product-item-wrapper')
    ADD_TO_CART = (By.CSS_SELECTOR, '.col-xl-12')
    CART_PAGE = (By.CSS_SELECTOR, '.bndl-shopping-bag')
    MAIN_PAGE = (By.CSS_SELECTOR, '.header-logo.img-logo')
    HEADER_CONTAINER = (By.CSS_SELECTOR, '.div-header-container')  # check for first page
    MEN_BREADCRUMB = (By.XPATH, "//span[@itemprop='name']")
    SIZE_SECTION = (By.XPATH, "//a[@data-tracking-label='BedenTablosu']")
    SIZE_CHOOSE = (By.XPATH, "//a[@size='M']")
    PAYMENT_PROCESS_CHECK = (By.XPATH, "//a[@data-tracking-label='Siparişi Tamamla']")

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.WEBSITE)
        self.wait = WebDriverWait(self.driver, 10)

    def test_LCW(self):
        assert self.wait.until(ec.presence_of_all_elements_located(self.HEADER_CONTAINER))[0].is_displayed()
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE_1))[1].click()

        time.sleep(2)
        erkekText = self.wait.until(ec.presence_of_all_elements_located(self.MEN_BREADCRUMB))[0].text
        assert erkekText == "Erkek", "This page doesnt contain Erkek BreadCrumb"
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[1].click() 

        time.sleep(2)
        bedenTablosu = self.wait.until(ec.presence_of_all_elements_located(self.SIZE_SECTION))[0].text
        assert bedenTablosu == 'Beden Tablosu', "This page doesnt contain Beden Tablosu"

        time.sleep(2)
        self.wait.until(ec.presence_of_all_elements_located(self.SIZE_CHOOSE))[0].click()

        time.sleep(2)
        self.wait.until(ec.presence_of_all_elements_located(self.ADD_TO_CART))[0].click()  

        time.sleep(2)
        self.wait.until(ec.presence_of_all_elements_located(self.CART_PAGE))[0].click()
        odemeAdimi = self.wait.until(ec.presence_of_all_elements_located(self.PAYMENT_PROCESS_CHECK))[0].text
        assert odemeAdimi == "ÖDEME ADIMINA GEÇ", "This page doesnt contain Proceed with Payment Button"

        time.sleep(2)     
        self.wait.until(ec.presence_of_all_elements_located(self.MAIN_PAGE))[0].click()
        assert self.wait.until(ec.presence_of_element_located(self.HEADER_CONTAINER)).is_displayed(), "You are not on the HomePage"
        time.sleep(2)     

if __name__ == "__main__":
    unittest.main()