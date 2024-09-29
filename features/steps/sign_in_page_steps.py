from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when ("Input email and password on SignIn page")
def input_email_and_password(context):
    context.app.sign_in_page.input_email_and_password('abney@diadiemmuasambienhoa.com', 'QQQqqq111')


@when ('Click "Sign in with password"')
def click_sign_in_with_password(context):
    context.app.sign_in_page.click_sign_in_with_password()


@then ('Verify user is logged in')
def verify_user_is_logged_in(context):
    context.app.sign_in_page.verify_user_is_logged_in()
