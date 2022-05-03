import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestEnterAnswer():

    # link = ['https://stepik.org/lesson/236895/step/1',
    # 'https://stepik.org/lesson/236896/step/1',
    # 'https://stepik.org/lesson/236897/step/1',
    # 'https://stepik.org/lesson/236898/step/1',
    # 'https://stepik.org/lesson/236899/step/1',
    # 'https://stepik.org/lesson/236903/step/1',
    # 'https://stepik.org/lesson/236904/step/1',
    # 'https://stepik.org/lesson/236905/step/1']



    @pytest.mark.parametrize('links', ['https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'])
    def test_enter_the_correct_answer_link(self, browser, links):
        browser.get(links)
        answer = math.log(int(time.time()))
        browser.implicitly_wait(10)
        answer = math.log(int(time.time()))
        browser.find_element_by_tag_name("textarea").send_keys(str(answer))
        browser.find_element_by_css_selector(".submit-submission").click()
        browser.implicitly_wait(10)
        feedback = browser.find_element_by_css_selector('pre.smart-hints__hint')
        feedbackText = feedback.text
        assert "Correct!" == feedbackText, f"The answer is wrong"

