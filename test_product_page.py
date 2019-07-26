from .pages.product_page import ProductPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    name = page.get_product_name()
    #print (name)
    price = page.get_product_price()
    #print (price)
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_added_message(name, price)
    