from selenium import webdriver
import time

link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_id("button").click()

time.sleep(10)
browser.quit()



# неявные ожидания
# from selenium import webdriver
# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text
