from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators ():
    enter_form = (By. CSS_SELECTOR, "h2:nth-child(1)")
    register_form = (By.CSS_SELECTOR, "#register_form > h2")

