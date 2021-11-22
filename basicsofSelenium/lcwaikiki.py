from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class LCW:
    print("Selam2")
    CATEGORY_PAGE_1 = (By.CLASS_NAME, '.sf-with-ul') 
    PRODUCT_PAGE = (By.CLASS_NAME, '.product-item-wrapper')
    ADD_TO_CART = (By.CLASS_NAME, '.col-xl-12')
    CART_PAGE = (By.CLASS_NAME, '.header-cart')
    MAIN_PAGE = (By.CLASS_NAME, '.header-logo.img-logo')
    HEADER_CONTAINER = (By.CLASS_NAME, '.div-header-container') #check for first page
    MOST_SOLD = (By.CLASS_NAME, '.uzun.visible-lg.visible-md') #check for second page
    ADD_TO_CART_CHECK = (By.CLASS_NAME, '.col-xs-12"') #check for add to cart
    #MEN_BREADCRUMB = (By.xp, "//a[@href='/tr-TR/TR/urun-grubu/erkek']") # $x("//a[@href='/tr-TR/TR/urun-grubu/erkek']")[2]
    CART_PAGE_CHECK = (By.CLASS_NAME, '.cart-square-link')
    WEBSITE = "https://www.lcwaikiki.com/tr-TR/TR"
    # C:/seleniumdriver/chromedriver

    def __init__(self):
        print("Selam3")
        self.driver = webdriver.Chrome("C:/seleniumdriver/chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.WEBSITE)
        self.wait = WebDriverWait(self.driver, 15)
        print("Selam4")

    def test_navigate(self):
        assert self.wait.until(ec.presence_of_element_located(self.HEADER_CONTAINER))[0].is_displayed()
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE_1))[1].click()
        #assert self.wait.until(ec.presence_of_element_located(self.MEN_BREADCRUMB))[2].is_displayed()
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[1].click() # click the item
        assert self.wait.until(ec.presence_of_element_located(self.ADD_TO_CART_CHECK))[10].is_displayed()
        self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_SIZE_PAGE))[0].click()
        print("Selam5")
        # ürün eklendi ancak sonrasındaki kontrol nasıl yapılaiblir onu düşün. sepete git çıkıyor karşına ondan yürüyebilirsin.
        self.wait.until(ec.presence_of_all_elements_located(self.CART_PAGE))[0].click()
        assert self.wait.until(ec.presence_of_element_located(self.CART_PAGE_CHECK)).is_displayed()
        self.wait.until(ec.presence_of_all_elements_located(self.MAIN_PAGE))[0].click()
        assert self.wait.until(ec.presence_of_element_located(self.HEADER_CONTAINER)).is_displayed()

print("Selam1")
LCW().test_navigate()
print("Selam6")

