from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

from selenium.webdriver.support.ui import WebDriverWait


class PageObject(BasePage):
    def add_to_cart (self):
        go_to_cart = self.browser.find_element(*ProductPageLocators.bottom_add)
        #go_to_cart = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(*ProductPageLocators.bottom_add))  # Ожидание и поиск кнопки отправки ответа
        go_to_cart.click()
        print("Click!!!")
        #return LoginPage(browser=self.browser, url=self.browser.current_url) 
       
       
     
    def should_be_add_to_card(self):
        
        assert self.is_element_present(*ProductPageLocators.bottom_add), "Buttom  for adding  to card is not presented"


    def shoud_be_click_toaddcart(self):
        assert self.go_to_cart.click(), "No click"


    def element_has_added(self):
        added = self.browser.find_element(*ProductPageLocators.has_added_to_cart)
        
        product_name = self.browser.find_element(*ProductPageLocators.name_of_product)
       # assert added == "The shellcoder's handbook был добавлен в вашу корзину.", \
       # f"Wrong product, got {added} instead of 'The shellcoder's handbook был добавлен в вашу корзину.'"
        #assert product_name.text in added.text , "Названия товаров не совпадает"
        assert product_name.text == added.text, "Названия товаров не совпадает"
        

    def price_of_cart(self):
        check_price = self.browser.find_element(*ProductPageLocators.check_product_price)
        Product_Price = self.browser.find_element(*ProductPageLocators.product_price)
        
        print(Product_Price.text)
        print(check_price.text)
        assert Product_Price.text == check_price.text, "Стоимость не совпадает"
       # product_price = self.browser.find_element(
        #*ProductPageLocators.PRODUCT_PRICE)
        #print(product_price.text)
        #print(price.text)
        #assert product_price.text == price.text, "не равно"


    def should_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.has_added_to_cart), \
       "Success message is presented"
       
       
    def should_not_be_success_message(self):
         assert self.is_not_element_present(*ProductPageLocators.has_added_to_cart), \
       "Success message is presented,but should not be"
       
        
       
       
    def message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.has_added_to_cart), \
            "Success message is not disappeared"