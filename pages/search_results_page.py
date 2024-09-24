from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    CART_IS_EMPTY = (By.XPATH, "//h1[text()='Your cart is empty']")


    def verify_results(self, product):
        actual_result = self.driver.find_element(*self.SEARCH_RESULTS_HEADER).text
        assert product in actual_result, f'Expected {product}, got actual {actual_result}'


    def cart_is_empty(self):
        self.driver.find_element(*self.CART_IS_EMPTY)
