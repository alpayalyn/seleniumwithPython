from _typeshed import Self
from selenium.webdriver.support.select import Select
from selenium import webdriver
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

# page object design pattern
# All the object are moved to the homepage

class TestHomePage(BaseClass):

    def test_formSubmission(self):

        homePage = HomePage(self.driver)
        homePage.getName().send_keys("Rahul")
        homePage.getEmail().send_keys("Shetty")
        homePage.getCheckBox().click()
        # homePage.getGender is a locator
        self.selectOptionByText(homePage.getGender(), "Male")
        alertText = driver.find_element_by_css_selector("[class*='alert-success']").text
