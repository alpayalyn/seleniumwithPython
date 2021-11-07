# Locators my name and filling the blanks..

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://login.salesforce.com/")

driver.find_element_by_css_selector("#username").send_keys("Alpay") # by attribute which is username
driver.find_element_by_css_selector(".password").send_keys("qwe456") # by class
driver.find_element_by_link_text("Forgot Your Password?").click() # Its valid only if there is text as a link.

# //tagname[text()='xxx']
driver.find_element_by_xpath("//a[text()='Cancel']").click() # We don't usually prefer doing it by xpath because the text might be changed.
driver.find_element_by_xpath("//form[@name='login']/div[1]/label") # by using this method, first form tag chosen, because there are 3 div, we chose the [1]first. and / mean go to its child, and we went to label.
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text) # css way of writing the similar code.

#difference between rel xpath and abs xpath // abs start from the beginnign whole html code. rel xpath: related(shorter simpler)


#  SELECT DROPDOWN STATIC!!!
# select class provide the methods to handle the options in dropdown 
# if the select dropdown is STATIC -> You can rely on the select_by_visible approach or select by index.
# It might be sth DYNAMIC therefore, to be able to use, things like (0)th. index you need to be sure the data provided is STATIC!
# we assigned Select to dropdown object now we can control over tha object.

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

# SELECT DROPDOWN DYNAMIC!!!
# first of all we went to the section, where we will type in what we search. for ex. ind of india's
# After typing in "ind" what we get will be bunch of country names. So we wanted those country names to be stored in a variable, so that we can match with India and get it clicked.
# Assertion!!! because the page is not being refreshed after you typed in what you look for. how to assert then?
# So how we solved it; bcause value attribute of the section, is being updated constantly with your text. You can get the attribute value and compare it with India

driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)

countries = driver.find_element_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))


for country in countries:
    if country.text == "India":
        country.click()
        break
print(driver.find_element_by_id("autosuggest").text)
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"
