from itertools import product

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='orderPickupButton'][id*='addToCartButtonOrTextIdFor']")


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    # context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN)).click()


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_card(context):
    # context.driver.find_element(*ADD_TO_CART_BTN_SIDE_NAV).click()
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN_SIDE_NAV)).click()


@then('Verify that correct search result shows for {product}')
def verify_search(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f'Expected {product} got actual {actual_result}'



