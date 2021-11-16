#Implicit wait
#Explicit wait
import time

from selenium import webdriver
# pause the test for few seconds using Time class
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# when I put implicit wait as below, it means, my code will wait for 5sec till my python code works. 
# If the code works before 5secs, it will work, and if it wont work it will wait for 5 secs, to get work. If time will be longer than 5 secs it will fail
# if you think you have fast environment go with explicit, if you dont have well server use implicit.
driver.implicitly_wait(5)
# wait until 5 seconds if object is not displayed
# global 
driver.get("https://rahulshettyacademy.com/seleniumPracise/")
driver.find_element_by_css_selector("input.searc-keyword").send_keys("ber")
time.sleep(4)
# It will get the total numbers of the products and it will count them.
count = len(driver.find_element_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_element_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_elements_by_css_selector("img[alt='Car']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
