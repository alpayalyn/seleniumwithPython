from selenium import webdriver
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class TestRun(unittest.TestCase):
    WEBSITE = "https://www.lcwaikiki.com/tr-TR/TR"
    CATEGORY_PAGE_1 = (By.CSS_SELECTOR, '.sf-with-ul')
    PRODUCT_PAGE = (By.CSS_SELECTOR, '.product-item-wrapper')
    ADD_TO_CART = (By.CSS_SELECTOR, '.col-xl-12')
    CART_PAGE = (By.CSS_SELECTOR, '.header-cart')
    MAIN_PAGE = (By.CSS_SELECTOR, '.header-logo.img-logo')
    HEADER_CONTAINER = (By.CSS_SELECTOR, '.div-header-container')  # check for first page
    MOST_SOLD = (By.CSS_SELECTOR, '.uzun.visible-lg.visible-md')  # check for second page
    ADD_TO_CART_CHECK = (By.CSS_SELECTOR, '.col-xs-12"')  # check for add to cart
    # MEN_BREADCRUMB = (By.xp, "//a[@href='/tr-TR/TR/urun-grubu/erkek']") # $x("//a[@href='/tr-TR/TR/urun-grubu/erkek']")[2]
    CART_PAGE_CHECK = (By.CSS_SELECTOR, '.cart-square-link')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.WEBSITE)
        self.wait = WebDriverWait(self.driver, 3)

    def test_LCW(self):
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE_1))[1].click()
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[1].click()  # click the item
        self.wait.until(ec.presence_of_all_elements_located("1"))[0].click()
        self.wait.until(ec.presence_of_all_elements_located(self.CART_PAGE))[0].click()
        self.wait.until(ec.presence_of_all_elements_located(self.MAIN_PAGE))[0].click()


if __name__ == "__main__":
    unittest.main()