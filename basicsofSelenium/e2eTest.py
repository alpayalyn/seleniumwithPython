from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_xpath(//a['class=nav-link']).click() # Its valid only if there is text as a link.

products = driver.find_elements_by_xpath("//div[@class='card h-100']")    #parent child travels.

# /div/h4/a
# product = //div[@class='card h-100']  product is already assigned with this locator. Now we are sending specifically the Locators above to point out by using already defined locator.
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text # IMPORTANT! if you will start with // again it will start from the top of the HTML so, you should start with ""
    if productName == "Blackberry":
        # Add item if its name is Blackberry