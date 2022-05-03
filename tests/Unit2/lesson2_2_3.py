from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    sum = str(int(x)+int(y))

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(sum)

    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
