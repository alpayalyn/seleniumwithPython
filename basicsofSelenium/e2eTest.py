from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_xpath("//a['@class=nav-link']").click() # Its valid only if there is text as a link.

products = driver.find_elements_by_xpath("//div[@class='card h-100']")    #parent child travels.
# You can go forward by adding element by element to the variable that you defined a path which starts with "//" then u can just add rest according to where you want to head basically.
# /div/h4/a
# product = //div[@class='card h-100']  product is already assigned with this locator. Now we are sending specifically the Locators above to point out by using already defined locator.
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text # IMPORTANT! if you will start with // again it will start from the top of the HTML so, you should start with ""
    if productName == "Blackberry":
        # Add item if its name is Blackberry Add to Cart.
        # product = //div[@class='card h-100']
        # Basically by using same path above, we need to choose between div s and then button ->  /div/button
        product.find_element_by_xpath("div/button").click()

driver.find_elements_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("Germany")
