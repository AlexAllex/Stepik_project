from .base_page import BasePage
from .locators import LoginPageLocators
import pytest



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        #assert True
        assert "login" in self.browser.current_url, f"link is not part of url" 
        

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.enter_form), "Login form is not presented"
        # реализуйте проверку, что есть форма логина
        #assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.register_form), "Login link is not presented"
        #assert True