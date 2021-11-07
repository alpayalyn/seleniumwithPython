# Locators my name and filling the blanks..

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https:{{rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Alpay")
driver.find_element_by_css_selector("input[name='name']").send_keys("Alpaca") # There were 2 indexes in the arrays but because python starts reading from above it gets the correct one.
driver.find_element_by_name("email").send_keys("Alpay123")

driver.find_element_by_id("exampleCheck1").click() # I have selected the checkbox.

driver.find_element_by_xpath("//input[@type='submit']").click()  

print(driver.find_element_by_class_name("alert-success").text)  # Getting the text written in the class.
