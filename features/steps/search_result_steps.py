from itertools import product

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify that correct search result shows for {product}')
def verify_search(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f'Expected {product} got actual {actual_result}'
