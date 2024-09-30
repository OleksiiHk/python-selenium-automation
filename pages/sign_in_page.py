from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_PAGE_OPEN_TEXT = (By.XPATH, "//h1/span")
    EMAIL_FIELD_TEXT = (By.ID, "username")
    PASSWORD_FIELD_TEXT = (By.ID, "password")
    LOGIN_BTN = (By.ID, 'login')

    TERMS_AND_CONDITIONS_LINK = (By.CSS_SELECTOR, "[aria-label*='terms & conditions']")

    def verify_sign_in(self):
        # self.find_element(*self.SIGN_IN_PAGE_OPEN)
        self.verify_text('Sign into your Target account', *self.SIGN_IN_PAGE_OPEN_TEXT)


    def input_email_and_password(self, email, password):
        self.input_text(email, *self.EMAIL_FIELD_TEXT)
        sleep(2)
        self.input_text(password, *self.PASSWORD_FIELD_TEXT)
        sleep(2)


    def click_sign_in_with_password(self):
        self.click(*self.LOGIN_BTN)


    def verify_user_is_logged_in(self, username):
        self.verify_partial_text(username, *self.LOGIN_BTN)


    def open_sign_in_page(self):
        self.open('https://www.target.com/login')


    def click_target_terms_and_conditions_link(self):
        self.wait_to_be_clickable_click(*self.TERMS_AND_CONDITIONS_LINK)


    def verify_target_terms_and_conditions_page(self):
        self.verify_partial_url('terms-conditions')
