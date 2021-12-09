from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage

class HomePage:

    def __init__(self, driver): # I added driver after self, pass the argumant of the driver also.
        self.driver = driver # homePage = HomePage(self.driver) should be added into the test_E2E

    SHOP = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        # to be able to use your actual driver below, you need to create constructor
        self.driver.find_element(*HomePage.SHOP).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
        # return self.driver.find_element(*HomePage.SHOP) # class variable if it were used with self that would be with self. If you add * it will read "shop" as Tuple
    
