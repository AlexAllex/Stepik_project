from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators ():
    enter_form = (By. CSS_SELECTOR, "h2:nth-child(1)")
    register_form = (By.CSS_SELECTOR, "#register_form > h2")
    EMAIL_ADRESS = (By.ID, 'id_registration-email')
    PAROL = (By.ID, 'id_registration-password1')
    bottom_reg = (By.CSS_SELECTOR, "[name='registration_submit']")
    PAROL2 = (By.ID, "id_registration-password2")


class ProductPageLocators():
    bottom_add = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")

    has_added_to_cart = (By.CSS_SELECTOR, ".alertinner >strong")
    name_of_product = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    product_price = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    check_product_price = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-info  fade in"]/div[@class="alertinner "]/p/strong')
    should_not_be_success_mes = (By.CLASS_NAME, '.alertinner ')
    go_to_basket = (By.CSS_SELECTOR, ".btn-group > a.btn.btn-default")
    text_empty_basket = (By.ID, 'content_inner')
    
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    go_basket = (By.CLASS_NAME, '.btn-group')
    no_messssage_Product_in_basket = (By.ID, 'content_inner')
    no_Product_in_basket = (By.CLASS_NAME, ".alert.alert-safe.alert-noicon.alert-info.fade.in ")
    USER_ICON = (By.CLASS_NAME, 'alertinner.wicon')