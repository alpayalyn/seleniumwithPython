import pytest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# request is an instance for your fixture " when you declare an fixture, request will be its instance"
# before starting the test this part of code will be executed and the config will be handle at the beginning.

@pytest.fixture(scope="class")  # scope means we used the fixture at class level.
def setup(request):
    driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver # this is how you can pass the driver from your fixture to the test case (self. will be put in test case python file too)
    yield  # thanks to yield after the above code will be executed and then the main code will be executed in another python file and then below close
    driver.close()
