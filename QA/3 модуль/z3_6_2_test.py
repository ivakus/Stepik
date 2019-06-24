import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"]

@pytest.fixture(scope="function")
def browser():
    browser_ = webdriver.Chrome(r"C:\\Users\\Gazprom\\Downloads\\chromedriver.exe")
    yield browser_
    browser_.close()

@pytest.mark.parametrize('link', links)    
def test_stepik (browser, link):
    #link = "https://stepik.org/lesson/236897/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    text_ =  WebDriverWait(browser,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,".quiz-component .textarea")))
    text_.send_keys(str(answer))
    b_ = WebDriverWait(browser,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,".submit-submission")))
    b_.click()
    result_ = WebDriverWait(browser,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,".smart-hints__hint")))
    if result_:  
        assert result_.text == "Correct!", "Return result is {}".format(result_.text)


