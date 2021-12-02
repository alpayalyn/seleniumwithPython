from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

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

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Germany")))
driver.find_element_by_link_text("Germany").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()
successText = driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you!" in successText
driver.get_screenshot_as_file("screen.png")
