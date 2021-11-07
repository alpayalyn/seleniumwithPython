from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://login.salesforce.com/")

driver.find_element_by_css_selector("#username").send_keys("Alpay") # by attribute which is username
driver.find_element_by_css_selector(".password").send_keys("qwe456") # by class
driver.find_element_by_link_text("Forgot Your Password?").click() # Its valid only if there is text as a link.

driver.find_element_by_xpath("//a[text()='Cancel']").click() # We don't usually prefer doing it by xpath because the text might be changed.
driver.find_element_by_xpath("//form[@name='login']/div[1]/label") # by using this method, first form tag chosen, because there are 3 div, we chose the [1]first. and / mean go to its child, and we went to label.
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text) # css way of writing the similar code.

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

# Assertions and the way they work.

message = driver.find_element_by_class_name("alert-success").text

assert "success" in message # When we type that in, it looks for success part, in the text. and if it finds success in the text. it returns true. so assertion becomes true.

assert "asdfsdf" in message # this is going to fail.

