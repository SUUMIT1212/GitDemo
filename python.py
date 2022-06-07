
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

##inputEmail = driver.find_element(By.ID, "email")
inputEmail = driver.find_element_by_id("email")
inputEmail.send_keys("batchT9@credence.com")

inputPassword = driver.find_element_by_id("pass")
inputPassword.send_keys("Password@123")

## inputEmail = driver.find_element(By.NAME, "login")
## inputButton = driver.find_element_by_name("login")
## inputButton.click()

##driver.find_element_by_name("login").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[2]/div/div/input").click()



