from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators ():
    enter_form = (By. CSS_SELECTOR, "h2:nth-child(1)")
    register_form = (By.CSS_SELECTOR, "#register_form > h2")


class ProductPageLocators():
    bottom_add = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")

    has_added_to_cart = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1)")
    name_of_product = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    product_price = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    check_product_price = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-info  fade in"]/div[@class="alertinner "]/p/strong')
