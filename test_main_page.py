from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.login_guest
class TestLogunFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        
        
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()



def test_should_be_register_form(browser):
   link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
   page = MainPage(browser, link)
   page.open()
   login_page = LoginPage(browser, browser.current_url)
   login_page.should_be_login_page()
   page.should_be_login_link()
   
   
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_from_main_page()
    page.no_product_in_basket()
    page.no_message_product_in_basket()
    
    
    

