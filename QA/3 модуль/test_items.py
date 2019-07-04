import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def test_buttom_put_in_bascket (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    b_ = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")))
    b_.click()
    time.sleep(2)