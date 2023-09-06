
from pages.product_page import PageObject
import pytest
from pages.login_page import LoginPage


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageObject(browser, link)
    page.open()
    page.add_to_cart()   # выполняем метод страницы — переходим на страницу cart
    page.solve_quiz_and_get_code()
    page.element_has_added()
    page.price_of_cart()
    
    
@pytest.mark.xfail(reason="Сообщение об успешном добавлении товара должно существовать")   
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?"
    page = PageObject(browser, link)
    page.open()
    page.add_to_cart()
    page.should_be_success_message()
    
    
def test_guest_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?"
        page = PageObject(browser, link)
        page.open()
        page.should_not_be_success_message()
    
    

    
@pytest.mark.xfail(reason="Сообщение об успешном добавлении товара не должно изчезать")    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?"
    page = PageObject(browser, link)
    page.open()
    page.add_to_cart()
    page.message_is_disappeared()
    
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()
    
    
@pytest.mark.need_review   
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.go_to_login_page()
    
    
@pytest.mark.need_review    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.go_to_basket()
    page.no_message_product_in_basket()
    page.message_about_basket_is_empty()
    
    

#@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPageT():
  
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
          link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
          page = LoginPage(browser, link) 
          page.open()
          page.register_new_user()
          page.should_be_authorized_user()
          
        
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?"
        page = PageObject(browser, link)
        page.open()
        page.should_not_be_success_message()
        
        
    @pytest.mark.need_review   
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = PageObject(browser, link)
        page.open()
        page.add_to_cart()   # выполняем метод страницы — переходим на страницу cart
        page.solve_quiz_and_get_code()
        page.element_has_added()
        page.price_of_cart()
        
         
          




    
   
   
   

