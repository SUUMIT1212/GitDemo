import selenium.webdriver.support.select
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver.get("https://rahulshettyacademy.com/angularpractice")
#driver.get("https://login.salesforce.com/")
#driver.maximize_window()
#driver.find_element_by_css_selector("#username").send_keys("amit")
#driver.find_element_by_css_selector(".password").send_keys("shetty")
#driver.find_element_by_css_selector(".password").clear()
#driver.find_element_by_css_selector()
#driver.minimize_window()
#print(driver.title)
#print(driver.current_url)
#driver.close()
#driver.find_element_by_name("name").send_keys("Rahul")
#driver.find_element_by_id("exampleCheck1").click()
#driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/input").click()
#driver.find_elements_by_link_text("already have an account").click()
#time.sleep(5)
#driver.refresh()
#dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
#dropdown.Select_by_visible_text("Female")
#time.sleep(5)
#dropdown.selenium.select_by_index(0)


#driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
#driver.find_element_by_id("autosuggest").send_keys("ind")
#time.sleep(2)
#countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
#print(len(countries))
#for country in countries:
#    if country.text == "India":
#        country.click()
#        break


#print(driver.find_element_by_id("autosuggest").text)
#assert driver.find_element_by_id("autosuggest").get_attribute('value')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements_by_css_selector("input[type = 'checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    checkbox.click()
    assert checkbox.is_selected()