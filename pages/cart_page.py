from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import Page

class CartPage(Page):
    CART_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")



    def verify_cart_empty(self):
        self.verify_text('Your cart is empty', *self.CART_IS_EMPTY_TEXT)
        # self.driver.find_element(*self.CART_IS_EMPTY)