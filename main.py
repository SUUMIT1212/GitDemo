import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
#driver.get("http://www.facebook.com/")
#driver.get("https://rahulshettyacademy.com/Automationpractice")
#action = ActionChains(driver)
#menu = driver.find_element_by_id()
#action.move_to_element(menu).perform()
#child = driver.find_element_by_link_text()
#action.move_to_element(child).click().perform()

driver.get("https:/chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.maximize_window()
action =ActionChains(driver)
action.context_click(driver.find_element_by_id("double-click")).perform()
action.double_click(driver.find_element_by_id("double-click")).perform()
alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me"==alert.text
alert.accept()
