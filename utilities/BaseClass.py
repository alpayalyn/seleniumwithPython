import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage

@pytest.mark.usefixtures("setup")
class BaseClass:
    
    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
    # We are passing locator as well.
    # To be able to select any DropDown we can use this method.
        sel = Select(homePage.getGender())
        sel.select_by_visible_text(text)