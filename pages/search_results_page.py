from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='orderPickupButton'][id*='addToCartButtonOrTextIdFor']")

    def verify_results(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS_HEADER)
        # actual_result = self.driver.find_element(*self.SEARCH_RESULTS_HEADER).text
        # assert product in actual_result, f'Expected {product}, got actual {actual_result}'


    def verify_results_url(self, product):
        self.verify_partial_url(product)


    def click_add_to_cart(self):
        self.wait_to_be_clickable_click(*self.ADD_TO_CART_BTN)
        # sleep(10)

    def side_nav_click_add_to_cart(self):
        self.wait_to_be_clickable_click(*self.ADD_TO_CART_BTN_SIDE_NAV)