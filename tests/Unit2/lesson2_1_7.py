from selenium import webdriver
import time
import math

def calculdateFn(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_id("treasure")
    x_element = treasure.get_attribute("valuex")
    y = calculdateFn(x_element)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
