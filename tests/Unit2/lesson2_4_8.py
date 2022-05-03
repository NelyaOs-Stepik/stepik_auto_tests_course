from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

button = browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_id("input_value")
x = x_element.text

y = calc(x)

input = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input)
input.send_keys(y)

button2 = browser.find_element_by_id("solve").click()

time.sleep(10)
browser.quit()

























# явные ожидания
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text
