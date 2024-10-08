from itertools import product

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.app.search_results_page.click_add_to_cart()

@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.app.search_results_page.side_nav_click_add_to_cart()
    sleep(2)

@then('Verify that correct search result shows for {product}')
def verify_search(context, product):
    context.app.search_results_page.verify_results(product)
    # actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    # assert product in actual_result, f'Expected {product} got actual {actual_result}'


@then('Verify product {product} in URL')
def verify_results_url(context, product):
    context.app.search_results_page.verify_results_url(product)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)
