from selenium import webdriver
# it can be an interview question, as well. 
# whenever you see tag names like this; iframe, frameset, frame that means there is a frame in the page.
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
# either frame id or frame id or index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am able to automate")
# If you want to come back and look for locators in website. You must switch back to default content like below.
driver.switch_to_default_content()
#after above code you will be able to perform the below.
print(driver.find_element_by_tag_name("h3").text)