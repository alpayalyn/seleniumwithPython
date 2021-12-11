from _typeshed import Self
from selenium.webdriver.support.select import Select
from selenium import webdriver
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
import pytest
from TestData.HomePageData import HomePageData

# page object design pattern
# All the object are moved to the homepage

class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["lastname"])
        homePage.getCheck().click()
        # homePage.getGender is a locator
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.submitForm().click()
        alertText = homePage.getSuccessMessage().text
        self.driver.refresh()

    @pytest.fixture(params=[HomePageData.test_HomePage_Data]) # By using ths function we will be able to send data into setup many times in an order. It was designed as Tuple at first. But now we turned it into Dictionary.
    def getData(self, request):
        return request.param