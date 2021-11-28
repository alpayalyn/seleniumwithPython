"""
- Validate whether products selected in Page1 are showing in page 2 check page
- Verify if Price decreases on Discount
- Verify if sum of products in checkout page matches with Total Amount

"""
import time
from selenium import webdriver
import unittest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class TestRun(unittest.TestCase):
    WEBSITE = "https://rahulshettyacademy.com/seleniumPractise/#/"
    listbut = []
    listveg = []
    amounts = []

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.WEBSITE)
        self.wait = WebDriverWait(self.driver, 10)

    def test_GreenKart(self):
        self.driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
        time.sleep(1)
        count = len(self.driver.find_elements_by_xpath("//div[@class='product-action']/button"))
        print(count)

        assert count == 3 
        butons = self.driver.find_elements_by_xpath("//div[@class='product-action']/button") # We are assigning all of locators. and there are 3 same button elements. so it will create 3 elemnts as array

        for buton in butons:
            time.sleep(1)
            buton.click()
            self.listbut.append(buton.find_element_by_xpath("parent::div/parent::div/h4").text) # this will help to get what is written in buton element. the whole function is: ("//div[@class='product-action']/button/parent::div/parent::div/h4")
        print(self.listbut)

        time.sleep(1)
        self.driver.find_element_by_css_selector("img[alt='Cart']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
        time.sleep(1)
        
        veggies =  self.driver.find_elements_by_css_selector("p.product-name") # critical way to compare texts of items in cart page and payment page
        for veg in veggies:
            time.sleep(1)
            self.listveg.append(veg.text)
        print(self.listveg)
        assert self.listbut == self.listveg, "Items were bought are not same"

        discountEarlier =  self.driver.find_element_by_css_selector("span.discountAmt").text
        time.sleep(1)
        self.driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
        time.sleep(1)
        self.driver.find_element_by_css_selector("button[class='promoBtn']").click()
        time.sleep(2)
        discountAfter = self.driver.find_element_by_css_selector("span.discountAmt").text
        assert not discountEarlier == discountAfter

        self.amounts = self.driver.find_elements_by_xpath("//tbody/tr/td[5]/p")
        totalAmount = 0
        
        for amount in self.amounts:
            totalAmount = totalAmount + int(amount.text)
        print(totalAmount)

        time.sleep(2)








        

if __name__ == "__main__":
    unittest.main()

