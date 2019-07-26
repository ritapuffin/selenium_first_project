from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.CLASS_NAME, "login_form")
    
class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")#.alertinner strong:nth-child(1)
    NAME = (By.CSS_SELECTOR, "#content_inner h1")
    ALERT_ADDED = (By.CSS_SELECTOR, ".alertinner strong")