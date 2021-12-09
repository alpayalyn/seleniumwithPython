from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver): # I added driver after self, pass the argumant of the driver also.
        self.driver = driver # homePage = HomePage(self.driver) should be added into the test_E2E
    
    # driver.find_elements_by_css_selector(".card-title a")
    # first create the specific object as the variable of the class
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-title a")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")
    
    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def checkOutItems(self):
        return self.driver.find_elements(*CheckoutPage.checkOut)
