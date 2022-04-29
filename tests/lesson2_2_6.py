from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    y = calc(x)

    input = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox").click()
    radiobutton = browser.find_element_by_id("robotsRule").click()

    button = browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(5)
    browser.quit()
