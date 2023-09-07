
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def no_product_in_basket(self):
         assert not self.is_element_present(*BasePageLocators. no_Product_in_basket),\
        "товары в корзине есть"
        
        
    def no_message_product_in_basket(self):
      
        assert not self.is_element_present(*BasePageLocators.no_messssage_Product_in_basket),\
        "нет текста о том, что корзина пуста"
        
        
    def is_disappeared(self, how, what, timeout=4):     #Если же мы хотим проверить, что какой-то элемент исчезает
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
            until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
        
    
    