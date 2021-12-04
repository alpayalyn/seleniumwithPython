# Create a separate file for each web page
# The test case file should contain only the test logic only.
# Create directories(folders) for Web Pages and Test Cases.

from selenium import webdriver
from Pages.MainPage import MainPage
from Pages.EnglishPage import EnglishPage


driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
baseURL = "https://www.wikipedia.org"

def set_up():
    driver.get(baseURL)

def test_main_page():
    mp = MainPage(driver)
    mp.test_title()
    mp.click_english_link()

def test_english_page():
    ep = EnglishPage(driver)
    ep.searchText()

set_up()
test_main_page()
test_english_page()


