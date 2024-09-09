from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from sample_script import driver


@given('Open target.com')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Click on Cart icon')
def click_on_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/icons/Cart.svg#Cart']").click()
    sleep(5)

@then('Verify “Your cart is empty” message is shown')
def verify_cart(context):
    context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")

 # # # # # # # # # # # # # # # # #v
@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    sleep(5)


@when('From right side navigation menu, click Sign In')
def click_sign_in_second(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(5)

@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.driver.find_element(By.XPATH, "//h1/span")




# @when('Search for a product')
# def search_product(context):
#     context.driver.find_element(By.ID, 'search').send_keys('tea')
#     driver.find_element(By.XPATH, "//button[@aria-label='search']").click()
#     sleep(5)
#
# @then('Verify that correct search result show')
# def verify_search(context):
#     actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#     expected_result = 'tea'
#     assert expected_result in actual_result, f'Expected {expected_result} got actual {actual_result}'


