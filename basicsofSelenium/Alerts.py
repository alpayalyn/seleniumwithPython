# selenium can only handle HTML
# for the pop ups which are written generally in java or javascript we use different method then html
# first we use alert switch_to method

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://https://www.lcwaikiki.com/tr-TR/TR")

driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.accept()

alert.dismiss()