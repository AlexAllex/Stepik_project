from pages.main_page import MainPage
from pages.product_page import PageObject
import pytest
from selenium import webdriver
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait





def test_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageObject(browser, link)
    page.open()
    #browser.implicitly_wait(20)
    print('кликнул')
    
    page.add_to_cart()   # выполняем метод страницы — переходим на страницу cart
    page.solve_quiz_and_get_code()
    page.element_has_added()
    page.price_of_cart()
    print("Корзина?")
    
   
   
   

# находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_te

