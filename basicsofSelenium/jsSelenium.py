# Look into that... Didn't work at once. 65.
# JS DOM can access any elements on wep page just like how selenium does. 
# Selenium have a method to execute javascript code in it.
# if you are not able to indentify the element by selenium methods. You can use document.getElements ... available methods  on the console and can get what You need by that.
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("alpay")
print.execute_script('return document.getElementsByName("name")[0].value')

