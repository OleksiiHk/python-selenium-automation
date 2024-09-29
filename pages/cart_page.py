from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import Page

class CartPage(Page):
    CART_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    CART_HAS_ITEM = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")


    def verify_cart_empty(self):
        self.verify_text('Your cart is empty', *self.CART_IS_EMPTY_TEXT)
        # self.driver.find_element(*self.CART_IS_EMPTY)

    def open_cart(self):
        self.open('https://www.target.com/cart')

    def verify_cart_item(self, number):
        self.verify_partial_text(number, *self.CART_HAS_ITEM)