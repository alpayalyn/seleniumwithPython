# JS DOM can access any elements on wep page just like how selenium does. 
# Selenium have a method to execute javascript code in it.
# if you are not able to indentify the element by selenium methods. You can use document.getElements ... available methods  on the console and can get what You need by that.
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("alpay")
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

# Sometimes Selenium cant choose or click the element you want to. Because while you ar ehovering ove rit some other pop up or elements get in the way so to prevent it. Java script executer 
# will be handling it on the HTML level.

shopButton = driver.find_element_by_css_selector("a[href*='shop']")
# second is : Locator you want to target, it all will be stored in arguments. by doing arguments[0], shopButton will be accessible./ if it will be arguments[1], shopButton, ShopClick then it will et ShopClick
# we just took the locator above, but we are clicking by Javascript DOM not by selenium
# We didnt use any selenium .click() but it will still work, but this time by JS executer. by firing HTML Event.
# we can use JS by using below code.
driver.execute_script("arguments[0].click();", shopButton)
# scrolling is not supported by selenium, so we will get it scrolled by using JS.
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")