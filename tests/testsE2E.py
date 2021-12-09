from _typeshed import Self
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

# @pytest.mark.usefixtures("setup") by navigating to the parent class which is a class we created in another folder,
# it will go there and this file will use that class's @pytest.mark.usefixtures feature.

class TestOne(BaseClass):

    def test_E2E(self):

        # MAKE IT MORE READABLE ;;; Only once we created an object like below row, for different page types, we defined their intsances in their own Methods and after that, in the E2E we assigned those instances to the next step's instances.    
        homePage = HomePage(self.driver) # we removed one of the locators in our test case, and handled it by using page object. Like this self driver assignment, we need to do, other pages' in their pageObject files.
        checkOutPage = homePage.shopItems() # this instance is like a check Point. We have come so far(Homepage is done) OK with this now we can proceed to checkout page.
        # checkOutPage = CheckoutPage(self.driver) No more required because we defined the object in CheckOutPage
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        confirmPage = checkOutPage.checkOutItems().click() # At this point we are done with checkout so we can proceed with  Confirm Page, so I assign this to Confirm.
        self.driver.find_element_by_id("country").send_keys("Germany")
        


        self.driver.find_element_by_xpath("//a['@class=nav-link']").click() # Its valid only if there is text as a link.
        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")    #parent child travels.
        # You can go forward by adding element by element to the variable that you defined a path which starts with "//" then u can just add rest according to where you want to head basically.
        # /div/h4/a
        # product = //div[@class='card h-100']  product is already assigned with this locator. Now we are sending specifically the Locators above to point out by using already defined locator.
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text # IMPORTANT! if you will start with // again it will start from the top of the HTML so, you should start with ""
            if productName == "Blackberry":
                # Add item if its name is Blackberry Add to Cart.
                # product = //div[@class='card h-100']
                # Basically by using same path above, we need to choose between div s and then button ->  /div/button
                product.find_element_by_xpath("div/button").click()

        self.driver.find_elements_by_css_selector("a[class*='btn-primary']").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("Germany")

        wait = self.WebDriverWait(self.driver, 7)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Germany")))
        self.driver.find_element_by_link_text("Germany").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        successText = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successText
        self.driver.get_screenshot_as_file("screen.png")
