from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname").send_keys("Nelya")
    input2 = browser.find_element_by_name("lastname").send_keys("Osnova")
    input3 = browser.find_element_by_name("email").send_keys("nel.os@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lesson.txt')
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button = browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(5)
    browser.quit()
