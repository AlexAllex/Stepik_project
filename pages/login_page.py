from .base_page import BasePage
from .locators import LoginPageLocators
import pytest
from mimesis import Person
from mimesis.locales import Locale
import time



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
      
        assert "login" in self.browser.current_url, f"link is not part of url" 
        

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.enter_form), "Login form is not presented"
        # реализуйте проверку, что есть форма логина
        

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.register_form), "Login link is not presented"
       
        
        
    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        email_adress = self.browser.find_element(*LoginPageLocators.EMAIL_ADRESS)
        email_adress.send_keys(email)
        password = str(time.time()) + "@fakepassword.org"
        parol = self.browser.find_element(*LoginPageLocators.PAROL)
        parol.send_keys(password)
        parol2 =self.browser.find_element(*LoginPageLocators.PAROL2)
        parol2.send_keys(password)
        time.sleep(15)
        self.browser.find_element(*LoginPageLocators.bottom_reg).click()
        



    
     