from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify “Your cart is empty” message is shown')
def verify_cart(context):
    context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")


@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.driver.find_element(By.XPATH, "//h1/span")


@then('Verify cart has {number} item')
def verify_cart_item(context, number):
    total_in_cart = context.driver.find_element(By.XPATH, "//div[./span[contains(text(), 'subtotal')]]").text
    assert f'{number} item' in total_in_cart, f"Expected {number} item but got {total_in_cart}"
