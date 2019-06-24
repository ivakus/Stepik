from selenium import webdriver
import time
"""
Чтобы получить максимальное количество баллов, прежде чем отправлять решение на рецензию, самостоятельно убедитесь в том что: 
Тест успешно проходит на странице http://suninjuly.github.io/registration1.html﻿
Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html
Используемые селекторы должны быть уникальны

"""

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome(r"C:\\Users\\Gazprom\\Downloads\\chromedriver.exe")
browser.get(link)
time.sleep(2)
el = browser.find_element_by_xpath('//div[@class="first_block"]/div[1]//input')
el.send_keys("Ivan")

el = browser.find_element_by_xpath('//div[@class="first_block"]/div[2]//input')
el.send_keys("Ivanov")

el = browser.find_element_by_xpath('//div[@class="first_block"]/div[3]//input')
el.send_keys("robot@robot.robot")

el = browser.find_element_by_css_selector("input.second")
el.send_keys("Ivan")

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)
welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
