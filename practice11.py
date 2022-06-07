from itertools import product
from logging import root
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count==3
buttons =driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()


