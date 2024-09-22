from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify “Your cart is empty” message is shown')
def verify_cart(context):
    context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")

@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.driver.find_element(By.XPATH, "//h1/span")
