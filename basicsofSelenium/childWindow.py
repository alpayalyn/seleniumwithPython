from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
driver.get("https://the-internet.herokuapp.com/windows")

time.sleep(2)
driver.find_element_by_link_text("Click Here").click()
childWindow = driver.window_handles[1] # We assigned the second window to childWindow and now we can switch to 2nd window but how? Like below.


driver.switch_to.window(childWindow)
print(driver.find_element_by_tag_name("h3").text) # On the second page we took h3
driver.close()

driver.switch_to.window(driver.window_handles[0]) # Changed back to first.
print(driver.find_element_by_tag_name("h3").text)
